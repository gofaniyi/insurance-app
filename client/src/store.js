import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import axios from 'axios';
import router from '@/router';

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [
        createPersistedState({
            storage: {
                getItem: key => localStorage.getItem(key),
                setItem: (key, value) => localStorage.setItem(key, value),
                removeItem: key => localStorage.removeItem(key)
            }
        })
    ],
    state: {
        api: 'http://localhost:5000/api/v1',
        user: null,
        isAuthenticated: false,
        companies: [],
        riskTypes: []
    },
    mutations: {
        setRecipes(state, payload) {
            state.recipes = payload;
        },
        setUser(state, payload) {
            state.user = payload;
        },
        setIsAuthenticated(state, payload) {
            state.isAuthenticated = payload;
        },
        setUserRecipes(state, payload) {
            state.userRecipes = payload;
        },
        setCompanies(state, payload) {
            state.companies = payload;
        },
        setRiskTypes(state, payload){
            state.riskTypes = payload;
        }
    },
    actions: {
        userLogin({ state, commit }, { email, password }) {
            let path = `${state.api}` + '/users/login';
            axios.post(path, {email : email, password : password})
                .then(res => {
                    let data = res.data.data;
                    let user = data.user;
                    user.token = data.token;
                    commit('setUser', user);
                    commit('setIsAuthenticated', true);
                    router.push('/risk-types');
                })
                .catch((error) => {
                    if (error.response) {
                        if (error.response.status == 401) {
                            alert(error.response.data.message);
                            return;
                        }
                    }
                    commit('setUser', null);
                    commit('setIsAuthenticated', false);
                    router.push('/');
                });
        },
        userRegister({ state, commit }, {companyId, email, password }) {

            let path = `${state.api}` + '/users/signup';
            axios.post(path, { companyId: companyId, email : email, password : password })
                .then(res => {
                    let data = res.data.data;
                    let user = data.user;
                    user.token = data.token;
                    commit('setUser', user);
                    commit('setIsAuthenticated', true);
                    router.push('/risk-types');
                })
                .catch((error) => {
                    if (error.response) {
                        if (error.response.status == 409) {
                            alert(error.response.data.message);
                            return;
                        }
                    }
                    commit('setUser', null);
                    commit('setIsAuthenticated', false);
                    router.push('/');
                });
        },
        userSignOut({ state, commit }) {
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };

            let path = `${state.api}` + '/users/logout';
            axios.post(path, {}, { headers: headers });
            commit('setUser', null);
            commit('setIsAuthenticated', false);
            router.push('/');
        },
        updateRiskType({ state, commit }, payload) {
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };

            let path = `${state.api}` + '/risk-types/' + payload.id;

            axios.put(path, payload, { headers: headers })
                .then(res => {
                    alert('Risk type updated successfully');
                    router.push('/risk-types');
                })
                .catch((error) => {
                    if (error.response) {
                        alert(error.response.data.message);
                        return;
                    }
                });
        },
        addRiskType({ state, commit }, payload) {
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };

            let path = `${state.api}` + '/risk-types';

            axios.post(path, payload, { headers: headers })
                .then(res => {
                    alert('Risk type created successfully');
                    router.push('/risk-types');
                })
                .catch((error) => {
                    if (error.response) {
                        alert(error.response.data.message);
                        return;
                    }
                });
        },
        addRisk({ state, commit }, payload) {
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };

            let path = `${state.api}` + '/risks';

            axios.post(path, payload, { headers: headers })
                .then(res => {
                    alert('Risk created successfully');
                    router.push('/risk-types');
                })
                .catch((error) => {
                    if (error.response) {
                        alert(error.response.data.message);
                        return;
                    }
                });
        },
        deleteRiskType({ state, commit }, riskTypeId) {
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };

            let path = `${state.api}` + '/risk-types/' + riskTypeId;
            axios.delete(path, { headers: headers })
                .then(res => {
                    alert('Risk type deleted successfully');
                    router.go();
                })
                .catch((error) => {
                    if (error.response) {
                        alert(error.response.data.message);
                        return;
                    }
                });
        },
        getCompanies({ state, commit }) {
            let path = `${state.api}` + '/companies';
            return axios.get(path)
                .then(res => {
                    commit('setCompanies', res.data.data);
                })
                .catch((error) => {
                });
        },
        getRiskTypes({ state, commit }) {
            let path = `${state.api}` + '/risk-types';
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };

            return axios.get(path, { headers: headers })
                .then(res => {
                    commit('setRiskTypes', res.data.data);
                })
                .catch((error) => {
                });
        }
    },
    getters: {
        isAuthenticated(state) {
            return state.user !== null && state.user !== undefined;
        },
        user(state) {
            return state.user;
        }
    }
});
