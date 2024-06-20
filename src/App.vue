<template>
  <div id="app">
    <HomeView />
  </div>
</template>

<script>
import HomeView from './views/HomeView.vue'

export default {
  name: 'App',
  components: {
    HomeView
  }
}
</script>

<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: var(--darkpink);

  --darkpink: #FF0A54;
  --lightpink: #FF8DAB;
  --pink: #FF487F;
  --lightpurple: #C77CF9;
  --darkpurple: #B450F7;
}

/* fonts */
h1 {
  font-size: 2.5em;
}
h2 {
  font-size: 2em;
}
h3 {
  font-size: 1.5em;
}
p {
  font-size: 1em;
  font-weight: 100;
}


/* buttons */
.default-button {
  background-color: var(--pink);
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  font-size: 0.7em;
  margin-right: 20px;
  margin-left: 20px;
  border-radius: 10%;
}
.default-button:hover {
  background-color: var(--lightpink);
}
.default-button:active {
  background-color: var(--lightpink);
  font-weight: 400;
}

</style>
