<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        permanent
        color="teal-darken-3"
        density="compact"
        rail
      >
        <br />
        <v-img
          width="300"
          :aspect-ratio="2"
          src="./src/assets/Vector.png"
        ></v-img>
        <br />

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <router-link to="/">
            <v-list-item prepend-icon="mdi-home-city"></v-list-item>
          </router-link>

          <router-link to :href="'http://localhost/8000/admin'">
            <v-list-item prepend-icon="mdi mdi-tune-vertical"></v-list-item>
          </router-link>

          <v-divider></v-divider>

          <v-list-group prepend-icon="mdi mdi-hexagon-slice-6">
            <template v-slot:activator="{ props }">
              <v-list-item v-bind="props"></v-list-item>
            </template>

            <router-link to="/">
              <v-app-bar-nav-icon size="x-small">N2</v-app-bar-nav-icon>
              <v-list-item></v-list-item>
            </router-link>

            <router-link to="/">
              <v-app-bar-nav-icon size="x-small">N5</v-app-bar-nav-icon>
              <v-list-item></v-list-item>
            </router-link>
          </v-list-group>

          <router-link to="/">
            <v-list-item
              prepend-icon="mdi mdi-hexagon-multiple-outline"
            ></v-list-item>
          </router-link>

          <router-link to="/">
            <v-list-item
              prepend-icon="mdi mdi-database-eye-outline"
            ></v-list-item>
          </router-link>
        </v-list>
      </v-navigation-drawer>
      <v-navigation-drawer :rail="rail">
        <br />
        <v-img
          src="logoscapelogoclair.png"
          alt="logo"
          max-height="125"
          cover
        ></v-img>
        <template v-slot:prepend>
          <v-btn
            variant="tonal"
            icon="mdi-chevron-left"
            @click.stop="rail = !rail"
            size="x-small"
            color="grey"
          >
            <template v-slot:prepend>
              <v-app-bar-nav-icon size="small"></v-app-bar-nav-icon>
            </template>
          </v-btn>
        </template>
        <v-list>
          <v-list-item title="Home" value="home"></v-list-item>

          <v-list-item title="Contacts" value="contacts"></v-list-item>

          <v-list-item title="Settings" value="settings"></v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      rail: true,
    };
  },
};
</script>
