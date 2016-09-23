<?php
$string = ' {"level":17,"modu":"3","map":["11122","21102","10000","01112","11200"],"pieces":["..XX,.XX.,XX..,.X..","X.X.,XXXX,.X..","XXX,.X.,.X.","X...,X.XX,XXX.","X,X,X,X,X",".X...,XXXXX,X..X.","X..,XXX","XXX,X.X,X..","XX,X."]}';
$array = json_decode($string,true);
$pieces = $array['pieces'];
$piece_array = array();
$map = $array['map'];
shuffle($pieces);
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
cal($piece_array,0,$map);
//testAddMaps();





function cal($piece_array,$t,$map){
    global $position_array,$row,$column;
    $positions = getMaxPosition($piece_array[$t],$row,$column);
    list($x,$y) = $positions;

    for($i = 0;$i<=$x;$i++){
        for($j = 0;$j<=$y;$j++){
            $position_array[$t] = $i.",".$j;
            if($t+1 >= count($piece_array)){
                //开始计算
                $resultMap = addMaps($map,$position_array,$piece_array,$row,$column);
                $re = check($resultMap);
                if($re ==0){
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