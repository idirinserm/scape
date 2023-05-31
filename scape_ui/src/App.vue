<template class="flex flex-center">
  <MapCom />
  <Sidebar />
  <router-view></router-view>
</template>

<script>
import Sidebar from "./components/SidebarCom.vue";
import MapCom from "@/components/MapCom.vue";

export default {
  name: "App",
  components: {
    MapCom,
    Sidebar,
  },
};
</script>

<style lang="scss">
.logo {
  position: absolute;
  width: 30%;
}

.line {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  top: 18%; /* moves the element down 50% of the viewport height */
  height: 8px;
  width: 70%;
  background: linear-gradient(
    to right,
    rgb(144, 207, 204),
    rgba(201, 212, 194, 1),
    rgba(225, 176, 132, 1),
    rgba(229, 106, 25, 1)
  );
  border-radius: 50px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #38a174;
}
</style>
