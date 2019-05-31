<template>
    <v-container>
        <v-flex mt-3 mb-5>
            <div class="col-sm-10">
                <h2 v-if="currentRiskType">{{currentRiskType.name}} Risk Type</h2>
            </div>
        </v-flex>

        <v-card class="pa-5">
            <v-flex xs6 offset-xs3 mb-5>
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-dialog v-model="dialog" persistent max-width="290">
                        <v-card>
                            <v-card-title class="body-2">Error</v-card-title>
                            <v-divider></v-divider>
                            <v-card-text>
                                <div v-for="(error, index) in errors" :key=index>
                                    {{error}}
                                </div>
                            </v-card-text>
                            
                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn  color="primary darken-1" @click="dialog = false">Ok</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-text-field v-model="name" :counter="15" :rules="nameRules" label="Name" required></v-text-field>

                    <v-flex mt-3>
                        <v-toolbar>
                            <v-toolbar-title>Custom Attributes</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                    </v-flex>

                    <v-container>
                        <v-layout v-for="(field, index) in fields" v-bind:key="index">
                            <v-flex xs12 md7>
                            <v-text-field
                                label="Field name"
                                v-model="field.name"
                                :rules="[v => !!v || 'A field name is required']"
                                value=""
                                required
                            ></v-text-field>
                            </v-flex>

                            <v-flex xs12 md4>
                                <v-select menu-props="right" v-model="field.type" :items="items" item-text="name" item-value="id" v-on:change="confirmChoices($event, field.name)" :rules="[v => !!v || 'Field type is required']" label="Field Type"
                                required>
                                </v-select>
                                <v-text-field v-if="isChoices[field.name]"
                                    label="e.g. blue,red,black"
                                    v-model="field.choices"
                                    value=""
                                    required
                                ></v-text-field>
                            </v-flex>

                            <v-flex xs12 md1>
                                <v-menu bottom left>
                                    <template v-slot:activator="{ on }">
                                    <v-btn
                                        green
                                        icon
                                        v-on="on"
                                    >
                                        <v-icon>more_vert</v-icon>
                                    </v-btn>
                                    </template>
                                    <v-list>
                                        <v-list-tile>
                                        <v-checkbox p3
                                    v-model="field.mandatory"
                                    label="Required? "
                                    ></v-checkbox>
                                        </v-list-tile>
                                    </v-list>
                                </v-menu>
                            </v-flex>
                            

                            <v-flex xs12 md1>
                                <v-btn icon>
                                    <v-icon color="red" @click="removeField(index)">delete</v-icon>
                                </v-btn>
                            </v-flex>

                        </v-layout>
                    </v-container>

                    <v-btn outline color="success" @click="addAttribute">
                        <v-icon left dark>add</v-icon>Add Attribute
                    </v-btn>
                    

                    
                    <v-layout mt-4>
                        <v-btn :disabled="!valid" color="success" @click="validate">
                            Save
                        </v-btn>
                        <v-btn outline color="success" to="/risk-types">
                            Cancel
                        </v-btn>
                    </v-layout>
                    
                </v-form>
            </v-flex>
        </v-card>
        

    </v-container>
</template>

<script>

import axios from 'axios';

  export default {
    data: () => ({
        blockRemoval: true,
        enableCustomAttSection: false,
        open: false, 
        fields: [],
        valid: true,
        name: '',
        nameRules: [
            v => !!v || 'Name is required',
            v => (v && v.length <= 15) || 'Name must be less than 15 characters'
        ],
        sides: [
            { title: 'Required Field' },
        ],
        items: [
            {name: 'text', id: 'text'},
            {name: 'number', id: 'number'},
            {name: 'radio button', id: 'radio button'},
            {name: 'text area', id: 'textarea'},
            {name: 'dropdown', id: 'dropdown'},
            {name: 'date', id: 'date'}
        ],
        isChoices: {},
        currentRiskType: null,
        errors: null,
        dialog: false
    }),
    computed: {
        currentUser() {
            return this.$store.getters.user;
        }
    },
    watch: {
        fields () {
            this.blockRemoval = this.fields.length <= 1
        }
    },
    methods: {
        getARiskType() {
            let state = this.$store.state;
            let path = `${state.api}` + '/risk-types/' + this.$route.params.id;
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };
            return axios.get(path, {headers: headers})
                .then(res => {

                    this.currentRiskType = res.data.data;

                    let customAttributes = res.data.data.customAttributes;

                    this.name = res.data.data.name;

                    let fields = [];
                    let isChoices = {};

                    customAttributes.forEach(function(attribute){

                        fields.push({
                            name: attribute.label,
                            type: attribute.inputControl,
                            mandatory: attribute.isRequired,
                            choices: attribute.choices || null
                        });

                        isChoices[attribute.label] = attribute.choices ? true : false;
                    })

                    this.fields = fields;

                    this.isChoices = isChoices;
                    
                })
                .catch((error) => {
                });
        },
        confirmChoices (e, index) {
            let status = false;
            if (['dropdown', 'radio button'].indexOf(e) >= 0) {
                status = true;
            }
            this.isChoices[index] = status;
        },
      validate () {
        if (this.$refs.form.validate()) {

            var payload = {
                id: this.currentRiskType.id,
                name: this.name,
                customAttributes: []
            };
            let customAttributes = [];
            let errors = [];
            let fieldNames = [];


            this.fields.forEach(function(field) {

                
                if (fieldNames.includes(field.name)) {
                    errors.push(field.name + ' is entered more than once');
                }

                let fieldData = {
                    key: field.name,
                    label: field.name,
                    inputControl: field.type,
                    isRequired: field.mandatory ? field.mandatory : false,
                };

                fieldNames.push(field.name);
                

                if (['dropdown', 'radio button'].indexOf(field.type) >= 0) {
                    
                    if (!field.choices) {
                        fieldData['choices'] = [];
                    }else if(typeof field.choices === 'string') {
                        fieldData['choices'] = field.choices ? field.choices.split(',') : [];
                    }else{
                        fieldData['choices'] = field.choices;
                    }
                }

                customAttributes.push(fieldData);
            });

            payload.customAttributes = customAttributes;

            if (errors.length > 0) {
                this.errors = errors;
                this.dialog = true;
                return;
            }


            this.$store.dispatch('updateRiskType', payload);

        }
      },
      addAttribute () {
          
          let checkEmptyFields = this.fields.filter(field => field.name === null || field.type === null)
          
          if (checkEmptyFields.length >= 1 && this.fields.length > 0) return

          this.enableCustomAttSection = true;

          this.fields.push({
            name: null,
            type: null,
            mandatory: null,
            choices: null
          });
      },
      removeField (lineId) {
            if (!this.blockRemoval) this.fields.splice(lineId, 1);
        }
    },
    created () {
        this.getARiskType();
    }
}
</script>