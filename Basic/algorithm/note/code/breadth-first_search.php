<?php

function personIsSeller($name)
{
    return $name[-1] == 'm';
}

function enqueue(SplQueue $queue, array $persons)
{
    foreach ($persons as $person) {
        $queue->enqueue($person);
    }
}

function search($name)
{
    global $graph;
    $searchQueue = new SplQueue();
    enqueue($searchQueue, $graph[$name]);
    $searched = [];
    while (!$searchQueue->isEmpty()) {
        $person = $searchQueue->dequeue();
        if (!isset($searched[$person])) {
            if (personIsSeller($person)) {
                printf('%s is a mango seller', $person);
                return true;
            } else {
                enqueue($searchQueue, $graph[$person]);
                $searched[$person] = true;
            }
        }
    }
    return false;
}

$graph = [];
$graph["you"] = ["alice", "bob", "claire"];
$graph["bob"] = ["anuj", "peggy"];
$graph["alice"] = ["peggy"];
$graph["claire"] = ["thom", "jonny"];
$graph["anuj"] = [];
$graph["peggy"] = [];
$graph["thom"] = [];
$graph["jonny"] = [];

search('you');

