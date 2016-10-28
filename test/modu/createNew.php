<?php
ini_set('memory_limit','1024M');
date_default_timezone_set('Asia/Shanghai');
$string_42 = '{"level":42,"modu":"2","map":["10011010","11011100","01110111","11111111","11101000","01111000","00010010","00001110"],"pieces":["XX,XX","X.XX.,XXXXX,XXX.X,XXX..,X....","..X,..X,X.X,XXX","..XXX,.XXX.,XXX..,.XXX.",".X.,.X.,XXX",".X...,.X...,XX...,XXXXX,...X.",".XXXX.,XXXXXX,..XXX.,...X..","X...,XXXX,..X.",".X,.X,XX,X.","X.XXX,XXXX.,XXX..,XXX..,X....","X.X,XXX,X.X",".XX...,XXXXXX,XXXX..","..X..,.XX..,.XXX.,XXXXX,..X..","...X.,XXXX.,.XXX.,.XXXX,..XXX","XX..,X...,XXX.,XXXX,.XXX","X..,XXX,..X","XX...,XXX..,..X..,.XXXX,.XXXX","XXXX"]}';
$string_45 = '{"level":45,"modu":"3","map":["00222202","01102001","02010000","21022101","22102001","02102000","21200210","22000110","21102000","00222200"],"pieces":["...X,...X,X..X,XXXX,XX.X",".XX.,XXXX,..X.,..XX,..X.","...X.,XXXXX,XX..X,....X",".XXX,.XXX,.XX.,.X..,XX..","....X,...XX,XXXXX,XXXX.,XXXX.",".XXX.,XXXXX,XXXX.,..XXX","XX.,.X.,.XX","..X.,.XXX,XXXX,X.XX,..X.",".XXX,XX.X,...X","XX...,XXXXX,XXXXX,XXXX.,...X.","...XX,XXXXX,XXXX.,.XXX.,..X..",".X.X.,.XXX.,XXXXX,XXXXX,..X..","XX...,.X...,XXX..,.XXXX","...X,..XX,XXXX,.X..",".X..,XX..,.XX.,XXXX,XX..",".X..,XXXX,X.XX,XXX.,XX..","...XX,XXXXX,..XX.,..XX.",".X...,XXXX.,XXXXX,.XXXX,...XX","XXX..,.X...,XXX..,.XXXX,.X..."]}';
$string = $string_45;
$array = json_decode($string,true);
var_dump($array);
$pieces = $array['pieces'];
$map = $array['map'];

$row = count($map);
$column = strlen($map[0]);
$modu = $array['modu'];

$removeArray_42 = array(
    '.X.,.X.,XXX' => '5,4',
    'XX...,XXX..,..X..,.XXXX,.XXXX' => '2,2',
    '.XXXX.,XXXXXX,..XXX.,...X..' => '3,1',
    );
$removeArray = array(
    'XX...,.X...,XXX..,.XXXX' => '6,1',
    '....X,...XX,XXXXX,XXXX.,XXXX.' => '4,0',
    '.X...,XXXX.,XXXXX,.XXXX,...XX' => '4,0',
    // '.XXX.,XXXXX,XXXX.,..XXX' => '4,2',
    // '...X,...X,X..X,XXXX,XX.X' => '3,3',
    // '.XX.,XXXX,..X.,..XX,..X.' => '3,3',
    // '...X,..XX,XXXX,.X..' => '4,0',
    // 'XXX..,.X...,XXX..,.XXXX,.X...' => '3,0',
);
$newMap = $map;
$spPieces = array();
var_dump($newMap);
foreach($removeArray as $k=>$v){
    $spPieces[] = $k;
    $temp = explode(',',$k);
    $pieceT = array();
    foreach ($temp as $item){
        $item = str_replace('X','1',$item);
        $item = str_replace('.','0',$item);
        $pieceT[] = $item;
    }
$newMap = addToMap($newMap, $v, $pieceT, $row, $column);
}

$mapLen = count($newMap);
$lastL = 0;
for($i=$mapLen-1; $i>-1;$i --){
    if ($newMap[$i]==0){
        $lastL += 1;
    }else{
        break;
    }
}

$endNewMap = array_slice($newMap, 0, $mapLen-$lastL);
var_dump($endNewMap);
$newPieces = array_diff($pieces, $spPieces);
var_dump($newPieces);

$lastPieces = array();
foreach($newPieces as $np){
$lastPieces[] = $np;
}
var_dump($lastPieces);
$newArray = $array;
$newArray['level'] = 'sppp';
$newArray['map'] = $endNewMap;
$newArray['pieces'] = $lastPieces;
//var_dump($newArray);
var_dump(json_encode($newArray));
die("test ok ");
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