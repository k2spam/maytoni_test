<template>
    <section>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </section>
</template>

<style lang="scss" scoped>
section {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 40px;
    margin: 30px 0;

    div {
        width: 15px;
        height: 40px;
        margin: 0 1px;
        background: var(--m-loader-color);

        &:nth-child(1) {
            animation: wave 1.6s 0s ease infinite;
        }
        &:nth-child(2) {
            animation: wave 1.6s 0.2s ease infinite;
        }
        &:nth-child(3) {
            animation: wave 1.6s 0.4s ease infinite;
        }
        &:nth-child(4) {
            animation: wave 1.6s 0.6s ease infinite;
        }
        &:nth-child(5) {
            animation: wave 1.6s 0.8s ease infinite;
        }
    }

    @keyframes wave {
        0% {
            height: 40px
        }
        50% {
            height: 10px;
        }
        100% {
            height: 40px;
        }
    }
}
</style>