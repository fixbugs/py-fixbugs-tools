<?php
//$string = ' {"level":17,"modu":"3","map":["11122","21102","10000","01112","11200"],"pieces":["..XX,.XX.,XX..,.X..","X.X.,XXXX,.X..","XXX,.X.,.X.","X...,X.XX,XXX.","X,X,X,X,X",".X...,XXXXX,X..X.","X..,XXX","XXX,X.X,X..","XX,X."]}';
$string = '{"level":15,"modu":"3","map":["00220","20111","21101","10200","02022"],"pieces":[".X,XX","XXXX,X...","XX.,.XX,..X,..X,..X","XXX..,..XX.,...XX","...X,XXXX,..X.","XX,X.,X.","XX,.X,.X","XXX,.X.","X.,XX"]}';
//$string = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}';
$string = '{"level":26,"modu":"4","map":["032200","100310","232330","210230","232333","213230"],"pieces":["XX,.X",".XX,XX.","..X.,..X.,.XXX,XXXX,X...","XXX.,..XX,..X.","..X..,..X..,.XX..,XXXXX,..XX.","...X,.XXX,XX..","XX..,.XXX,.XX.,.X..","XXX,XXX,.XX,XX.,.X.",".XX,..X,XXX,XX.,.X.","..XX.,.XXXX,.XX..,XX...",".X...,XXXXX,...XX,...XX",".XX,XX.,XX.,.X.,.X."]}';
$array = json_decode($string,true);
$pieces = $array['pieces'];
$piece_array = array();
$map = $array['map'];
//shuffle($pieces);
foreach ($pieces as $piece){
        $temp = explode(',',$piece);
        $t = array();
        foreach ($temp as $item){
            $item = str_replace('X','1',$item);
            $item = str_replace('.','0',$item);
            $t[] = $item;
        }
        $piece_array[] = $t;
}
$postion_array = array();
$row = count($map);
$column = strlen($map[0]);
$modu = $array['modu'];
$map_array = array();
$start_time = microtime(true);
$total_count = 0;
cal($piece_array,0,$map);
//testAddMaps();


function cal($piece_array,$t,$map){
    global $position_array,$row,$column;
    $positions = getMaxPosition($piece_array[$t],$row,$column);
    list($x,$y) = $positions;

    for($i = 0;$i<=$x;$i++){
        for($j = 0;$j<=$y;$j++){
            global $total_count;
            $total_count += 1;
            if($total_count%10000000 == 0){
                global $start_time;
                var_dump($total_count);
                var_dump(microtime(true) - intval($start_time));
            }
            $position_array[$t] = $i.",".$j;
            if($t+1 >= count($piece_array)){
                //开始计算
                $resultMap = addMaps($map,$position_array,$piece_array,$row,$column);
                $re = check($resultMap);
                if($re ==0){
                    global $start_time;
                    global $pieces;
                    var_dump($pieces);
                    var_dump($piece_array);
                    var_dump( microtime(true)- intval($start_time) );
                    echo "<pre>";print_r($position_array);
                    $re6 = '';
                    foreach ($position_array as $p){
                        $re6 = $re6.str_replace(',','',$p);
                    }
                    echo $re6;
                    exit;
                }
                continue;
            }
            cal($piece_array,$t+1,$map);

        }
    }
}



function initMap($n,$m){
    $result = array();
    for($i=0;$i<$n;$i++){
        $result[] =   str_repeat('0',$m);
    }
    return $result;
}

function addToMap($map,$position,$piece,$row=3,$column =3){
    list($x,$y) = explode(',',$position);
    global $modu;
    for($i = $x;$i<$column,$i<$x+count($piece);$i++){
        $num= $piece[$i-$x];
        for($j = 0;$j<strlen($num);$j++){
            $map[$i][$j+$y] = (strval($num)[$j]+$map[$i][$j+$y])%$modu;
        }
    }
    return $map;
}
function getMaxPosition($piece,$row,$column){
    $x = $row-count($piece);
    $y = $column-strlen($piece[0]);
    return array($x,$y);
}
function check($map){
    $result = 0;
    foreach ($map as $item) {
        $result+=$item;
    }
    return $result;
}
function addMaps($map,$postions,$piece_array,$row=3,$column=3){
    $tmp = $map;
    foreach ($postions as $key =>$postion){
        $tmp = addToMap($tmp,$postion,$piece_array[$key],$row,$column);
    }
    return $tmp;
}

function testAddMaps(){
    $map = array('0000','0000','0001');
    $postions = array("3,2");
    $piece_array = array(array("1"));
    $tem = addMaps($map,$postions,$piece_array);
    echo "<pre>";print_r($tem);exit;
}