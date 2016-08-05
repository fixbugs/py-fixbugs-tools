<?php
/**
 * 日志模型
 * @category	Pub
 * @package		Pub.house.sina.com.cn
 * @copyright	Leju Publish Content System
 * @license		Leju Publish Content System license
 * @author		zhenjun@leju.com
 */

class log extends pubModel
{
    /**
     * 主键,可选
     * @var string
     */
    protected $_pk = 'id';
    
    /**
     * 表名
     * @var string
     */
    protected $_tableName = 'log';
    
    /**
     * 初始化函数
     * @param	void
     * @return	void
     */
    public function _initialize(){
        parent::_initialize();
    }
    
    /**
     * 日志对应的语言文件
     * @var string
     */
    protected $_language_file = 'log/log';
    
    /**
     * 增加日志信息
     * @param string $level	日志级别(警告、错误、通知)warning,error,notice
     * @param string $message 日志内容
     * @param mixed $params 附加内容(例如：当编辑时可以将当前编辑的内容存入跟踪表中)
     * @return array	array('status' => true/false, 'message'	=> 'string');
     */
    public function addLog($level='', $message='', $params=array()){
        $data = array();
        $return = false;
        $allow_level = C('log.php', 'allow_log_level');
    
        if(is_array($allow_level) && !in_array($level, $allow_level)){
            $error = T('"%s" level is not allow by log', $level);
            $return = array_for_result(false, $error);
        }else{
            $data['passport_id'] = USER_PASSPORT_ID;
            $data['level'] = $level;
            $data['message'] = $message;
            $data['params'] = json_encode($params);
            $data['createdate'] = _NOW_;
            $data['id'] = make_shard_id(CORE_VSID);
            $ret = $this->insert($data);
            if(!$ret){
                $error = T('log add fail! level:%s, message:%s', $level, $message);
                $return = array_for_result(false, $error);
            }else{
                $msg = T('log add success, level:%s, message:%s', $level, $message);
                $return = array_for_result(true, $msg);
            }
            return $return;
        }
    }
    
    /**
     * 根据参数获取系统log数据
     *
     * @param array $post	获取参数(级别，操作者，时间)
     * @return array	列表数据
     */
    public function getSearchList(array $post)
    {
    	$cond = Slae::criteria();
    	
    	$page = isset($post['page'])? intval($post['page']):1;
    	$size = isset($post['size'])? intval($post['size']):10;
    	if (!empty($post['word'])) {
    		$cond->add(array('message'=>$post['word']),'like');
    	}
    	$offset = $size * ($page-1);
    	$offset < 0 && $offset = 0;
    	$order = (isset($post['sort']) ? $post['sort'] : 'id DESC');
    	$cond->limit = $size;
    	$cond->offset = $offset;
    	$cond->order =  $order;
    	$logList = $this->findAll($cond);
    	$logList = getAttrFromModel($logList);
    	return $logList;
    }

    /**
	 * 导出日志ID信息
	 * @return bool
	 */
	public function exportId($limit=1000, $offset=0, $params=array()){
		$this->setDaoType(Leb_Model::DAO_TYPE_NONE);
		$cond = Slae::criteria();
		if($params){
			$cond->add(array('id'=>$params['max_id']), '<=');
		}
		$cond->limit = $limit;
		$cond->offset = $offset;
		$cond->order = 'id desc';
		$data = $this->findAll($cond);
		$data = getAttrFromModel($data);
		return $data;
	}
    
    /**
     * 删除日志信息
     * @param array|string $logid
     * @return bool
     */
    public function deleteLog($logid){
		if(empty($logid)){
			$this->setModelError(T('need valid log id'));
			return false;
		}
		$this->setDaoType(Leb_Model::DAO_TYPE_BOTH);
		//判断是否是多条删除,字符串=>'3,22,5'
		if(strpos(',', $logid)){
			$id = explode(",",trim($logid));
			$cond = Slae::criteria(array('id'=>$id));
			$ret = $this->deleteAll($cond);
		}else{
		    $ret = $this->deleteByPk($logid);
		}
		if($ret === false){ 
		    $this->setModelError(T('delete fail,error:%s',$this->getDbError()));
		    return false;
	    }else{
	       $this->setModelError(T('delete interface log %s successed',$logid));
	       return true;
	    }
	       
    }
}