<template>
    <nav class="navbar">
        <div class="navbar-left">
            <RouterLink to="/" class="navbar-logo">Pickle</RouterLink>
        </div>
        <div class="navbar-right">
            <button class="default-button">Analysis</button>
            <button class="default-button">Settings</button>
            <button class="default-button">
                <RouterLink to="/login" class="navbar-logo">Log In</RouterLink>
            </button>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'PickleNavbar'
    }

</script>

<style scoped>
    .navbar{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: -8px;
        margin-left: -8px;
        margin-right: -8px;
        background-color: var(--darkpink);
        border-bottom: 0.5px solid black;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        font-size: 2em;
    }
    .navbar-logo{
        text-decoration: none;
        color: white;
    }
    .navbar-left{
        display: flex;
        align-items: center;
        margin-left: 20px;
    }
    .navbar-right{
        display: flex;
        align-items: center;
        margin-right: 20px;
    }

</style>