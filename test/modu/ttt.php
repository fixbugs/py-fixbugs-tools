<?php
date_default_timezone_set('Asia/Shanghai');
$string_17 = ' {"level":17,"modu":"3","map":["11122","21102","10000","01112","11200"],"pieces":["..XX,.XX.,XX..,.X..","X.X.,XXXX,.X..","XXX,.X.,.X.","X...,X.XX,XXX.","X,X,X,X,X",".X...,XXXXX,X..X.","X..,XXX","XXX,X.X,X..","XX,X."]}';
$string_15 = '{"level":15,"modu":"3","map":["00220","20111","21101","10200","02022"],"pieces":[".X,XX","XXXX,X...","XX.,.XX,..X,..X,..X","XXX..,..XX.,...XX","...X,XXXX,..X.","XX,X.,X.","XX,.X,.X","XXX,.X.","X.,XX"]}';
$string_12 = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}';
$string_test = '{"level":12,"modu":"2","map":["0000","0000","0001","0110"],"pieces":["X","XX"]}';
$string_26 = '{"level":26,"modu":"4","map":["032200","100310","232330","210230","232333","213230"],"pieces":["XX,.X",".XX,XX.","..X.,..X.,.XXX,XXXX,X...","XXX.,..XX,..X.","..X..,..X..,.XX..,XXXXX,..XX.","...X,.XXX,XX..","XX..,.XXX,.XX.,.X..","XXX,XXX,.XX,XX.,.X.",".XX,..X,XXX,XX.,.X.","..XX.,.XXXX,.XX..,XX...",".X...,XXXXX,...XX,...XX",".XX,XX.,XX.,.X.,.X."]}';
//26 102110301130201001000012
$string_18 = '{"level":18,"modu":"2","map":["1010","0011","0101","1101","1110"],"pieces":["XX,.X",".X.,.X.,XXX","X.,XX,X.",".X..,XX..,.XXX,.XX.",".X.,XXX",".X..,XX..,XXXX,.X..",".X,.X,XX","X..,X..,XXX,XX.,X..","X.,X.,XX","X.,XX,.X"]}';
$string_19 = '{"level":19,"modu":"3","map":["0022","2102","1112","1111","2210"],"pieces":[".X,.X,XX,XX","XX,X.,X.","X.,XX","X..,XXX,.X.,.X.","XX,X.","XXX,..X","X.,X.,XX,.X,.X","XXXX","XX,X.","..X.,..X.,XXXX,...X"]}';
$string_27 = '{"level":27,"modu":"3","map":["21211","20220","20012","22002","22000"],"pieces":["XX.,X..,XXX","X..,XXX","XXX,X.X","..XX,..X.,XXX.","X..,XXX,X..",".X.,XXX,XX.",".X.,.XX,XX.,.X.","X,X,X,X","X,X,X","XX,XX","XXXX,..X.",".X,XX,X.",".XX,XX."]}';
$string_28 = '{"level":28,"modu":"2","map":["001110","001101","010100","011000","111000"],"pieces":["XXX,.X.,XX.,.X.","XX..,XX..,.XXX","XXXX,.X..","X..,X.X,XXX,X..",".X,XX,.X,.X","X....,XXXXX,.X...","X.,XX,X.","XXXX",".X.,XX.,.XX","XX.,XXX",".XXX,XX..","X,X,X,X","..X..,XXXXX"]}';
$string_29 = '{"level":29,"modu":"3","map":["202220","202112","220000","200201","211221","212001","021211"],"pieces":["XXXXX,XXXX.,XX...","..X.,.XX.,XXXX,X...","...X,..XX,.XX.,XX..",".X..,.XX.,XXX.,XXXX,.X..","XXX,..X,.XX","XXX,.XX,..X","X...,XXXX,XX..,.X..,.X..","...X,..XX,.XXX,..X.,XXX.",".X...,.X...,.XX..,XXXXX",".X..,XXXX,.XX.,..XX,...X",".X.,.XX,.X.,XX.,XX.","X.,XX,.X,.X",".X.,.XX,.X.,XX.,XXX"]}';
//29 11220021313300013122103301
$string_30 = '{"level":30,"modu":"2","map":["111000","000100","010101","110001","011010","100010","001111","111111"],"pieces":[".XXX,.XXX,.X..,XX..,XXX.","...XX,XX.X.,.XXXX,.XXX.","..X,.XX,XX.,.XX","..XX,..X.,.XXX,XXXX,..X.",".X,XX,XX,X.,XX","..X..,.XX..,.XXX.,XXXX.,...XX",".X,XX,.X,.X","X.X.,XXX.,..XX","...X.,..XX.,XXXXX","XXXX,...X","XXX,XX.,.XX,..X","XXXX.,..XXX,.XXXX,...X.","XX.,.XX,.X.","..X.,.XXX,XXX.,X.X.,X.X."]}';
$string = $string_26;
$array = json_decode($string,true);
var_dump($array);
$pieces = $array['pieces'];
$is_order_pieces = 1;
if($is_order_pieces){
    $old_pieces = $pieces;
    $pieces = orderPieces($pieces);
}
var_dump($pieces);
var_dump("--------split line pieces------------");
$piece_array = array();
$map = $array['map'];
//如果值为1则逆序暴力破解，否则正序破解
$is_rsort = 0;
//shuffle($pieces);
$piece_count_array = array();
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
$sp = 0;
foreach($pieces as $piece){
    $piece_count_array[] = lastPieceCounts($sp);
    $sp += 1;
}
var_dump($piece_count_array);
$position_array = array();
$row = count($map);
$column = strlen($map[0]);
$modu = $array['modu'];
$map_array = array();
$start_time = microtime(true);
$total_count = 0;
$end_result_map_string = endResultString($map);

$start_end_map = endResultMap($map);

$last_four_result = array();

endFourPiecesString();
die('test');

if($is_rsort){
    calRsort($piece_array,0,$map);
}else{
    cal($piece_array,0,$map);
}
//testAddMaps();


function cal($piece_array,$t,$map){
    global $position_array,$row,$column;
    $positions = getMaxPosition($piece_array[$t],$row,$column);
    list($x,$y) = $positions;
    $lastMap = $map;
    for($i = 0;$i<=$x;$i++){
        for($j = 0;$j<=$y;$j++){
            $position_array[$t] = $i.",".$j;
            if($t+1 >= count($piece_array)){
                global $total_count;
                $total_count += 1;
                if($total_count % 10000000 == 0){
                    var_dump($total_count);
                    var_dump(date('y-m-d h:i:s', time()));
                }
                $resultMap = addToMap($lastMap, $position_array[$t], $piece_array[$t], $row, $column);
                $re = check($resultMap);
                if($re ==0){
                    var_dump("-----------end-------------");
                    global $start_time;
                    global $pieces;
                    var_dump(date('y-m-d h:i:s', time()));
                    var_dump( microtime(true)- intval($start_time) );
                    var_dump($pieces);
                    echo "<pre>";print_r($position_array);
                    $re6 = '';
                    foreach ($position_array as $p){
                        $re6 = $re6.str_replace(',','',$p);
                    }
                    echo $re6;
                    echo "</pre>";
                    var_dump(stringResultGet($position_array));
                    exit;
                }else{
                    $map = $lastMap;
                }
                continue;
            }else{
                $map = addToMap($lastMap,$position_array[$t],$piece_array[$t],$row,$column);
                $checkNext = checkMapNeedContinue($map, $t);
                if(!$checkNext){
                    continue;
                }
                // if(intval($checkNext) == 4){
                //     var_dump($position_array);
                //     die("sppspp");
                // }
            }
            cal($piece_array, $t+1, $map);
        }
    }
}


function calRsort($piece_array,$t,$map){
    global $position_array,$row,$column;
    $positions = getMaxPosition($piece_array[$t],$row,$column);
    list($x,$y) = $positions;
    $lastMap = $map;
    for($i = $x;$i>=0;$i--){
        for($j=$y;$j>=0;$j--){
            $position_array[$t] = $i.",".$j;
            if($t+1 >= count($piece_array)){
                global $total_count;
                $total_count += 1;
                if($total_count % 10000000 == 0){
                    var_dump($total_count);
                    var_dump(date('y-m-d h:i:s', time()));
                }
                $resultMap = addToMap($lastMap, $position_array[$t], $piece_array[$t], $row, $column);
                // $checkNext = checkMapNeedContinue($resultMap, $t);
                // if($checkNext == 4){
                //     var_dump($position_array);
                //     var_dump($piece_array);
                //     exit(0);
                // }
                $re = check($resultMap);
                if($re ==0){
                    var_dump("-----------end-------------");
                    global $start_time;
                    global $pieces;
                    var_dump(date('y-m-d h:i:s', time()));
                    var_dump( microtime(true)- intval($start_time) );
                    echo "<pre>";print_r($position_array);
                    $re6 = '';
                    foreach ($position_array as $p){
                        $re6 = $re6.str_replace(',','',$p);
                    }
                    echo $re6;
                    echo "</pre>";
                    var_dump(stringResultGet($position_array));
                    exit;
                }else{
                    $map = $lastMap;
                }
                continue;
            }else{
                $map = addToMap($lastMap,$position_array[$t],$piece_array[$t],$row,$column);
                $checkNext = checkMapNeedContinue($map, $t);
                if(!$checkNext){
                    continue;
                }
                if($checkNext == 4){
                    var_dump($position_array);
                    var_dump($piece_array);
                    exit(0);
                }
            }
            calRsort($piece_array, $t+1, $map);
        }
    }
}


function initMap($n,$m){
    $result = array();
    for($i=0;$i<$n;$i++){
        $result[] = str_repeat('0',$m);
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

function checkMapNeedContinue($map, $nowPosition){
    global $piece_count_array;
    $mapNeedCounts = getMapNeedCounts($map);
    // if($mapNeedCounts<=4){
    //     var_dump($map);
    //     return 4;
    // }
    $lastPiecesMaxCounts = $piece_count_array[$nowPosition];
    if($mapNeedCounts > $lastPiecesMaxCounts){
        // var_dump($map);
        // var_dump($mapNeedCounts);
        // var_dump($nowPosition);
        // var_dump($lastPiecesMaxCounts);
        // var_dump($piece_count_array);
        // die('mapneedbigger');
        return false;
    }
    return true;
}

function getMapNeedCounts($map){
    global $row, $column, $modu;
    $needCounts = 0;
    for($i=0; $i<$row;$i++){
        for($j=0;$j<$column;$j++){
            $needCounts += ($modu - $map[$i][$j]) % $modu;
        }
    }
    return $needCounts;
}

function lastPieceCounts($nowPosition){
    global $piece_array;
    $maxL = count($piece_array);
    $lastMaxCounts = 0;
    for($i=$nowPosition+1;$i<$maxL;$i++){
        $lastMaxCounts += getPieceMaxCounts($piece_array[$i]);
    }
    return $lastMaxCounts;
}

function getPieceMaxCounts($piece){
    $x = count($piece);
    $y = strlen($piece[0]);
    $pieceMaxCounts = 0;
    for($i=0;$i<$x;$i++){
        for($j=0;$j<$y;$j++){
            $pieceMaxCounts += intval($piece[$i][$j]);
        }
    }
    return $pieceMaxCounts;
}

function getMaxPosition($piece,$row,$column){
    $x = $row-count($piece);
    $y = $column-strlen($piece[0]);
    return array($x,$y);
}
function check($map){
    global $end_result_map_string;
    $nowMapMd5 = md5(json_encode($map));
    if($end_result_map_string == $nowMapMd5){
        $result = 0;
        foreach ($map as $item) {
            if($item != 0){
                return 1;
            }
        }
        return $result;
    }
    return 1;
    // $result = 0;
    // foreach ($map as $item) {
    //     if($item != 0){
    //         return 1;
    //     }
    //  }
    // return $result;
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

function orderPieces($pieces){
    $lenArray = array();
    foreach($pieces as $p){
        $lenArray[] = strlen($p);
    }
    arsort($lenArray);
    $newPieces = array();
    foreach($lenArray as $k=>$v){
        $newPieces[] = $pieces[$k];
    }
    //var_dump($pieces);
    //var_dump($newPieces);
    return $newPieces;
}

function stringResultGet($position_array){
    global $pieces, $old_pieces;
    $keyArr = array();
    foreach($old_pieces as $p){
        $tmpKeys = array_keys($pieces, $p);
        if(count($tmpKeys) == 1){
            $keyArr[] = $tmpKeys[0];
        }else{
            foreach($tmpKeys as $tk){
                if(!array_keys($keyArr, $tk)){
                    $keyArr[] = $tk;
                }
            }
        }
    }
    $result = '';
    foreach($keyArr as $kp){
        $result = $result.str_replace(',','',$position_array[$kp]);
    }
    return $result;
}

function endResultString($map){
    $endMap = endResultMap($map);
    $endMapMd5 = md5(json_encode($endMap));
    return $endMapMd5;
}

function endResultMap($map){
    $row = count($map);
    $col = strlen($map[0]);
    $endMap = array();
    foreach ($map as $m){
        $endMap[] = str_repeat('0',$col);
    }
    return $endMap;
}

function endFourPiecesString(){
    global $piece_array, $last_four_result;
    $maxL = count($piece_array);
    $newPieceArray = array();
    for($i = $maxL-4;$i<$maxL;$i++){
        $newPieceArray[] = $piece_array[$i];
    }
    mapcal($newPieceArray, 0);
    var_dump(count($last_four_result) );
    die("sfjslkdjflk");
}

function mapcal($piece_array, $t=0, $position_array=array(), $resultArray=array()){
    if($t == count($piece_array)){
        return true;
    }
    global $start_end_map, $row, $column, $last_four_result;
    $positions = getMaxPosition($piece_array[$t],$row,$column);
    list($x,$y) = $positions;
    $tmp = array();
    for($i = 0;$i<=$x;$i++){
        for($j = 0;$j<=$y;$j++){
            $position_array[$t] = $i.",".$j;
            if($t+1>=count($piece_array)){
                $resultMap = addMaps($start_end_map, $position_array, $piece_array,$row,$column);
                $resultString = '';
                foreach ($position_array as $p){
                    $resultString = $resultString.str_replace(',','',$p);
                }
                $key = md5(json_encode($resultMap));
                $last_four_result[$key] = $resultString;
                $tmp[$key] = $resultString;
                getMerge($last_four_result, $tmp);
            }
            mapcal($piece_array, $t+1, $position_array, array_merge($tmp,$resultArray));
        }
    }

}

function getMerge(&$B, $tmp){
    $B = array_merge($B, $tmp);
}