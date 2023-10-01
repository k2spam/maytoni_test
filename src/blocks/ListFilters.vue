<script setup>
import { storeToRefs } from 'pinia';
import { useLightsStore } from '../stores/lights';

const { isNew } = storeToRefs(useLightsStore())
const { filterLigths } = useLightsStore()
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