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
        <div><img src="./assets/Jaye.png" alt="Jaye Logo" /></div>
        <div class="signIn">
          <p class="m-0">Already have an account?</p>
          <button class="btn-jaye ms-2">Sign in</button>
        </div>
      </header>
      <section>
        <div class="px-5" style="width: 40%">
          <h5 class="m-0">Create your account</h5>
          <p>Sign up for your #1 shopping Experience</p>
          <form action="">
            <label for="email" class="my-3">
              <input type="email" name="email" id="email" class="form-control" placeholder="Email"/>
            </label>
            <button type="submit" class="form-control btn-jaye">Next</button>
            <div class="mt-3.5">
              <button class="form-control d-flex justify-content-center mb-2">
                <svg
                  width="22"
                  height="22"
                  viewBox="0 0 22 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M21.2046 11.0219C21.2046 10.3102 21.1469 9.59469 21.0238 8.89453H11.1484V12.9262H16.8036C16.5689 14.2265 15.8149 15.3768 14.7108 16.1077V18.7237H18.0847C20.0659 16.9002 21.2046 14.2073 21.2046 11.0219Z"
                    fill="#4285F4"
                  />
                  <path
                    d="M11.149 21.2506C13.9727 21.2506 16.354 20.3234 18.089 18.7231L14.7152 16.1071C13.7765 16.7457 12.5647 17.1073 11.1528 17.1073C8.42141 17.1073 6.10549 15.2646 5.27453 12.7871H1.79297V15.4839C3.5703 19.0193 7.19036 21.2506 11.149 21.2506Z"
                    fill="#34A853"
                  />
                  <path
                    d="M5.27112 12.7874C4.83256 11.4871 4.83256 10.0791 5.27112 8.7788V6.08203H1.7934C0.308449 9.0404 0.308449 12.5258 1.7934 15.4842L5.27112 12.7874Z"
                    fill="#FBBC04"
                  />
                  <path
                    d="M11.149 4.45451C12.6416 4.43143 14.0842 4.99309 15.1653 6.0241L18.1544 3.03495C16.2617 1.25762 13.7496 0.280476 11.149 0.311252C7.19036 0.311252 3.5703 2.54253 1.79297 6.0818L5.27069 8.77857C6.0978 6.29724 8.41756 4.45451 11.149 4.45451Z"
                    fill="#EA4335"
                  />
                </svg>
                <span class="ms-2">Continue with Google</span>
              </button>
              <button class="form-control d-flex justify-content-center">
                <svg
                  width="19"
                  height="22"
                  viewBox="0 0 19 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M17.9768 16.5093C17.657 17.2414 17.2785 17.9153 16.84 18.5348C16.2422 19.3794 15.7527 19.9641 15.3755 20.2887C14.7908 20.8216 14.1643 21.0945 13.4934 21.1101C13.0117 21.1101 12.4309 20.9742 11.7548 20.6987C11.0765 20.4245 10.4531 20.2887 9.88313 20.2887C9.28534 20.2887 8.64422 20.4245 7.95846 20.6987C7.27165 20.9742 6.71836 21.1178 6.29534 21.132C5.652 21.1592 5.01075 20.8785 4.37067 20.2887C3.96213 19.9356 3.45114 19.3303 2.83899 18.4728C2.1822 17.557 1.64223 16.4951 1.21921 15.2845C0.766171 13.9768 0.539062 12.7105 0.539062 11.4846C0.539062 10.0804 0.845267 8.86919 1.45859 7.85424C1.94061 7.03899 2.58186 6.3959 3.38444 5.9238C4.18702 5.4517 5.05421 5.21112 5.9881 5.19573C6.49909 5.19573 7.16919 5.35236 8.00192 5.6602C8.8323 5.96907 9.36548 6.1257 9.59925 6.1257C9.77402 6.1257 10.3663 5.94255 11.3704 5.57742C12.32 5.2388 13.1214 5.09859 13.7779 5.15382C15.5569 5.2961 16.8935 5.99106 17.7823 7.2431C16.1913 8.19842 15.4042 9.53647 15.4199 11.253C15.4342 12.59 15.9237 13.7026 16.8856 14.586C17.3216 14.996 17.8084 15.3129 18.3501 15.538C18.2326 15.8756 18.1086 16.1989 17.9768 16.5093ZM13.8967 0.59889C13.8967 1.64684 13.5103 2.6253 12.7403 3.53096C11.8109 4.60761 10.6869 5.22975 9.46794 5.13158C9.45241 5.00585 9.4434 4.87354 9.4434 4.73449C9.4434 3.72847 9.88535 2.65182 10.6702 1.77151C11.062 1.3258 11.5603 0.95519 12.1647 0.659551C12.7677 0.368323 13.338 0.207268 13.8745 0.179688C13.8902 0.319782 13.8967 0.459898 13.8967 0.59889Z"
                    fill="black"
                  />
                </svg>
                <span class="ms-2">Continue with Apple</span>
              </button>
            </div>
          </form>
        </div>
      </section>
      <div class="floaty-container">
        <img src="./assets/Floaty.png" alt="Floaty" width="200px" height="200px">
      </div>
    </main>
  </div>
</template>

<style scoped>
main {
  font-family: 'Jost', system-ui;
  font-optical-sizing: auto;
  font-style: normal;
  position: relative;
}
header {
  display: flex;
  justify-content: space-between;
  padding: 10px 30px;
  border-bottom: 2px solid #f1f1f1;
}
.btn-jaye {
  color: white;
  background-color: #e9c46a;
  padding: 8.72px 21.8px;
  border: none;
  border-radius: 5.23px;
}
.signIn {
  display: flex;
  justify-content: center;
  align-items: center;
}
label {
  display: block;
}
section {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
  text-align: center ;
}
.floaty-container{
  position: absolute;
  right: 2rem;
  bottom: 1rem;
}
</style>
