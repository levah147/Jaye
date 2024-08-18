<!-- <script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style> -->

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <main>
      <header>
        <div><img src="./assets/Jaye.png" alt="Jaye Logo"></div>
        <div class="signIn"><p class="mr-2">Already have an account?</p> <button class="btn-jaye">Sign in</button></div>
      </header>
      <section></section>
    </main>
  </div>
</template>

<style scoped>
main{font-family: "Jost", system-ui;
  font-optical-sizing: auto;
  font-style: normal;
}
header{
  display: flex;
  justify-content: space-between;
  padding: 10px 30px;
  border-bottom: 2px solid #f1f1f1;
}
.btn-jaye{
  color:white;
  background-color: #E9C46A;
  padding: 8.72px 21.8px;
  border: none;
  border-radius: 5.23px;
}
.signIn{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>