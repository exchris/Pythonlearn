<?php
$graph = [];
$graph["start"] = [];
$graph["start"]["a"] = 6;
$graph["start"]["b"] = 2;
$graph["a"] = [];
$graph["a"]["fin"] = 1;
$graph["b"] = [];
$graph["b"]["a"] = 3;
$graph["b"]["fin"] = 5;
$graph["fin"] = [];
# the costs table
$infinity = PHP_INT_MAX;
$costs = [];
$costs["a"] = 6;
$costs["b"] = 2;
$costs["fin"] = $infinity;
# the parents table
$parents = [];
$parents["a"] = "start";
$parents["b"] = "start";
$parents["fin"] = null;
$processed = [];

function findLowestCodeNode($costs){
    $lowerCost = PHP_INT_MAX;
    $lowerCostNode = null;
    global $processed;
    foreach($costs as $node => $cost){
        if($cost< $lowerCost && !array_key_exists($node, $processed)){
            $lowerCost = $cost;
            $lowerCostNode = $node;
        }
    }
    return $lowerCostNode;
}

$node = findLowestCodeNode($costs);

while($node) {
    $cost = $costs[$node];
    $neighbors = $graph[$node];
    foreach(array_keys($neighbors) as $n){
        $newCost = $cost+$neighbors[$n];
        if ($costs[$n] > $newCost){
            $costs[$n] = $newCost;
            $parents[$n] = $node;
        }
    }
    $processed[$node] = true;
    $node = findLowestCodeNode($costs);
}


print("Cost from the start to each node:");
var_dump($costs);
