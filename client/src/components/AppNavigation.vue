<template>
    <span>
        <v-navigation-drawer app v-model="drawer" class="cyan lighten-2" dark disable-resize-watcher>
            <v-list>
                <template v-for="(item, index) in items">
                    <v-list-tile :key="index">
                        <v-list-tile-content>
                            {{item.title}}
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-divider :key="`divider-${index}`"></v-divider>
                </template>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar app color="cyan darken-3" dark>
            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>
            <v-spacer class="hidden-md-and-up"></v-spacer>
            <router-link to="/">
                <v-toolbar-title data-cy="titleBtn">{{appTitle}} 
                    <span v-if="isAuthenticated" class="subheading">({{currentUser.company.name}})</span>
                    </v-toolbar-title>
            </router-link>
            <div v-if="isAuthenticated" class="hidden-sm-and-down">
                <v-btn flat class="hidden-sm-and-down nav-menu" to="/risk-types" data-cy="riskTypesMenuBtn">Risk Types</v-btn>
                <v-btn flat class="hidden-sm-and-down nav-menu" to="/risks/add" data-cy="risksMenuBtn">Create Risk</v-btn>
            </div>
            <v-spacer class="hidden-sm-and-down"></v-spacer>
            <div v-if="!isAuthenticated" class="hidden-sm-and-down">
                <v-btn flat to="/sign-in" data-cy="signinBtn">Sign In</v-btn>
                <v-btn flat to="/register" class="nav-join" data-cy="registerBtn">Register</v-btn>
            </div>
            <div v-else>
                <span class="my-3">Hi, {{currentUser.email}}</span>
                <v-btn flat color="white" @click="logout" data-cy="logout">Logout</v-btn>
            </div>
        </v-toolbar>
    </span>
</template>

<script>
export default {
    name: 'AppNavigation',
    data() {
        return {
            appTitle: 'BriteCore',
            drawer: false,
            items: [
                { title: 'Sign In' },
                { title: 'Register' }
            ]
        };
    },
    computed: {
        isAuthenticated() {
            return this.$store.getters.isAuthenticated;
        },
        currentUser() {
            return this.$store.getters.user;
        }
    },
    methods: {
        logout() {
            this.$store.dispatch('userSignOut');
        }
    }
};
</script>

<style scoped>
a {
    color: white;
    text-decoration: none;
}
</style>
