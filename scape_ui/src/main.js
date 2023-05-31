import { createApp } from "vue/dist/vue.esm-bundler";
import { createStore } from "vuex";
import App from "./App.vue";
import router from "./router";

import OpenLayersMap from "vue3-openlayers";
import "vue3-openlayers/dist/vue3-openlayers.css";

import { maps } from "@/store/maps";

// Vuetify
import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import vClickOutside from "click-outside-vue3"

const vuetify = createVuetify({
  theme: {
    defaultTheme: "dark",
  },
  components,
  directives,
});

const store = createStore({
  modules: {
    maps,
  },
});

const app = createApp(App);
app.use(store);
app.use(router);
app.use(vuetify);
app.use(vClickOutside);
app.use(OpenLayersMap);
app.mount("#app");
