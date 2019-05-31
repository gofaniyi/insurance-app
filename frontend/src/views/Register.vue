<template>
    <v-container fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Register New User</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form ref="form" v-model="valid" lazy-validation>
                            <v-select prepend-icon="account_balance" :items="companies" item-text="name" item-value="id" label="Company" v-model="companyId" solo></v-select>
                            <v-text-field prepend-icon="person" name="email" label="Email" type="email"
                                          v-model="email" :rules="emailRules" data-cy="registerEmailField" required>
                            </v-text-field>
                            <v-text-field prepend-icon="lock" name="password" label="Password"
                                          type="password" required v-model="password" :rules="passwordRules"
                                          data-cy="registerPasswordField">
                            </v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" class="mb-2" :disabled="!valid" @click="submit" data-cy="registerSubmitBtn">Register</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
/* eslint-disable */
export default {
    name: 'Register',
    data() {
        return {
            valid: false,
            email: '',
            password: '',
            companyId: '',
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+/.test(v) || 'E-mail must be valid'
            ],
            passwordRules: [
                v => !!v || 'Password is required',
                v =>
                    v.length >= 6 ||
                    'Password must be greater than 6 characters'
            ]
        };
    },
    methods: {
        submit() {
            if (this.$refs.form.validate()) {
                this.$store.dispatch('userRegister', {
                    companyId: this.companyId,
                    email: this.email,
                    password: this.password
                });
            }
        },
        getCompanies() {
            this.$store.dispatch('getCompanies');
        }
    },
    computed: {
        companies() {
            return this.$store.state.companies;
        }
    },
    mounted() {
        this.getCompanies();
    }
};
</script>

<style scoped>
</style>
