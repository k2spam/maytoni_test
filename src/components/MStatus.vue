<script setup>
</script>

<template>
    <div>
        <slot></slot>
    </div>
</template>

<style lang="scss" scoped>
    div {
        display: flex;
        align-items: center;
        justify-content: space-around;
        width: 70px;
        height: 70px;
        border: 1px solid var(--m-border-color);
        border-radius: 50%;
    }
</style>