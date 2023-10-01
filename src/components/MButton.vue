<script setup>
</script>

<template>
    <button><slot></slot></button>
</template>

<style lang="scss" scoped>
button {
    padding: 7px 15px;
    background: var(--vt-c-white);
    border: 1px solid var(--m-border-color);
    border-radius: 5px;
    cursor: pointer;

    &:active {
        background: var(--m-bg-color);
    }
}
</style>