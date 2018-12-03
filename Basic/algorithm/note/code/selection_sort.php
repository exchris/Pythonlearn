<?php

/**
 * 选择排序
 */
function findSmallest($arr)
{
    $smallest = $arr[0];
    $smallestIndex = 0;
    $length = count($arr);
    for ($i = 0; $i < $length; $i++) {
        if ($arr[$i] < $smallest) {
            $smallest = $arr[$i];
            $smallestIndex = $i;
        }
    }
    return $smallestIndex;
}

function selectionSort($arr)
{
    $newArr = [];
    $length = count($arr);
    for ($i = 0; $i < $length; $i++) {
        $smallest = findSmallest($arr);
        array_push($newArr, array_splice($arr, $smallest, 1)[0]);
    }
    return $newArr;
}

var_dump(selectionSort([5, 3, 6, 2, 10]));
