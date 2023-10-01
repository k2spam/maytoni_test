<script setup>
import { storeToRefs } from 'pinia';
import { useLightsStore } from '../stores/lights';

import MButton from '../components/MButton.vue';

const { isNew, dtsort } = storeToRefs(useLightsStore())
const { filterLigths, sortByDate } = useLightsStore()
</script>

<template>
    <article>
        <label>
            <input 
                v-model="isNew"
                @change="filterLigths"
                type="checkbox" 
                >
            <span>только новинки</span>
        </label>
        <MButton @click="sortByDate">
            Сортировать дате 
            {{ dtsort > 0 ? '&#8593;' : '&#8595;' }}
        </MButton>
    </article>
</template>

<style lang="scss" scoped>

article {
    margin: 0 0 20px;
    padding: 10px 20px;
    border: 1px solid var(--m-border-color);
    background: var(--m-bg-color);
    border-radius: 5px;
    label {
        margin: 0 10px 0 0;
        input {
            vertical-align: middle;
        }
        span {
            margin-left: 7px;
            vertical-align: middle;
            user-select: none;
        }
    }
}
</style>