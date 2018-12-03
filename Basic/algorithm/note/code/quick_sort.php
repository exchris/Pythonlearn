<?php

/**
 * 快速排序
 */
function quicksort($array){
    if(count($array)<2){
        return $array;
    } else {
        $pivot = $array[0];

        $less =  array_filter(array_slice($array,1),function($el) use ($pivot){ return $el<= $pivot;});

        $greater = array_filter(array_slice($array,1),function($el) use ($pivot){return $el>$pivot;});
        return array_merge(quicksort($less),[$pivot],quicksort($greater));
    }
}


var_dump(quicksort([10,5,2,3]));
