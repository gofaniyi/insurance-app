<template>
    <v-container>
        <v-flex mt-3 mb-5>
            <div class="col-sm-10">
                <span>{{getCurrentRiskTypeId}}</span>
                <h2>New Risk</h2>
            </div>
        </v-flex>

        <v-flex xs7>
            <v-stepper v-model="e1">
                <v-stepper-header>
                <v-stepper-step :complete="e1 > 1" step="1">Select Risk Type</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="2">Fill Information</v-stepper-step>

                </v-stepper-header>

                <v-stepper-items>
                <v-stepper-content step="1">
                    
                    <v-select
                    :items="riskTypes" 
                    item-text="name" item-value="id" label="Risk Type" 
                    v-model="riskTypeId" :value=getCurrentRiskTypeId></v-select>

                    <v-btn
                    color="primary"
                    @click="completeStep1"
                    >
                    Next
                    </v-btn>
                </v-stepper-content>

                <v-stepper-content step="2">
                    <v-form ref="form" v-model="valid" lazy-validation>
                        <v-alert v-if="errors" :value="true" color="error" icon="warning" outline>
                            Can't submit form, see the errors below
                            <br/>
                            <div v-for="(error, index) in errors" :key=index>
                                {{error}}
                            </div>
                        </v-alert>
                        <v-layout v-for="(field, index) in customAttributes" v-bind:key="index">
                            <!-- Text: Input Control  -->
                            <v-text-field v-if="field.inputControl == 'text'" :id=field.key v-model="risk[field.key]" 
                            :label=field.label :required=field.isRequired></v-text-field>
                            
                            <!-- Number: Input Control  -->
                            <v-text-field v-if="field.inputControl == 'number'" :id=field.key v-model.number="risk[field.key]" 
                            :label=field.label :required=field.isRequired type="number"></v-text-field>

                            <!-- Text: Input Control  -->
                            <v-textarea v-if="field.inputControl == 'textarea'" v-model="risk[field.key]" 
                            :label=field.label></v-textarea>

                            <!-- Radio Button: Input Control  -->

                            <v-radio-group v-if="field.inputControl == 'radio button'" v-model="risk[field.key]" row>
                                <template v-slot:label>
                                    <div>{{field.label}}</div>
                                </template>
                                <v-radio v-for="choice in field.choices" :key="choice" :name="field.key" :label="choice" :value="choice"></v-radio>
                            </v-radio-group>
                            
                            <!-- Dropdown: Input Control  -->
                            <v-select v-if="field.inputControl == 'dropdown'" :items="field.choices" :label="field.label" v-model="risk[field.key]"></v-select>

                            <!-- Date: Input Control  -->
                            <v-layout v-if="field.inputControl == 'date'" row wrap>
                                <v-flex xs12 sm6 md4>
                                <v-dialog
                                    ref="menu"
                                    v-model="dialog[field.key]"
                                    :return-value.sync="date"
                                    persistent
                                    lazy
                                    full-width
                                    width="290px"
                                    :key="field.key"
                                >
                                    <template v-slot:activator="{ on }">
                                    <v-text-field
                                        v-model="risk[field.key]"
                                        :label="field.label"
                                        prepend-icon="event"
                                        readonly
                                        v-on="on"
                                    ></v-text-field>
                                    </template>
                                    <v-date-picker v-model="risk[field.key]" scrollable>
                                    <v-spacer></v-spacer>
                                    <v-btn flat color="primary" @click="closeDateWidget(field)">Cancel</v-btn>
                                    <v-btn flat color="primary" @click="$set(dialog, field.key, false)">OK</v-btn>
                                    </v-date-picker>
                                </v-dialog>
                                </v-flex>
                            </v-layout>

                        </v-layout>
                        
                    </v-form>

                    <v-btn flat outline @click="e1 = 1" v-if="showBackBtn">Back</v-btn>

                    <v-btn
                    color="primary"
                    @click="completeStep2"
                    >
                    Save
                    </v-btn>

                    <v-btn outline color="success" v-if="showCancelBtn" :to="`/risk-types/`+riskTypeId+`/risks`">
                        Cancel
                    </v-btn>

                    
                </v-stepper-content>
                </v-stepper-items>
            </v-stepper>
        </v-flex>
        
        

    </v-container>
</template>

<script>

  export default {
    data: () => ({
        valid: true,
        e1: 0,
        riskTypeId: '',
        customAttributes: [],
        date: new Date().toISOString().substr(0, 10),
        menu: false,
        modal: false,
        risk: {},
        dialog: {},
        errors : null,
        showCancelBtn: false,
        showBackBtn: true,
    }),
    computed: {
        currentUser() {
            return this.$store.getters.user;
        }
    },
    methods: {
        closeDateWidget (field) {
            this.dialog[field.key] =  false;
            this.risk[field.key] = null;
        },
        completeStep1 () {
            
            if(this.riskTypeId){

                let filtered = this.riskTypes.filter(el => el.id == this.riskTypeId);
                
                this.customAttributes = filtered ? filtered[0].customAttributes : [];

                let attributes = {};

                this.customAttributes.forEach(function(attribute){
                    attributes[attribute.key] = null;
                })

                this.risk = attributes;
                this.errors = null;

                this.e1 = 2;
            }else{
                alert('You have to select a risk type');
            }
            
        },
        completeStep2 () {
            let errors = [];

            for (const [key, value] of Object.entries(this.risk)) {

                let filteredFields = this.customAttributes.filter(el => el.key == key);
            
                let field = filteredFields ? filteredFields[0] : null;
                

                if(field.isRequired && !value){
                    errors.push(field.label + ' is required.')
                }
            }

            let payload = {data: this.risk};
            payload['riskTypeId'] = this.riskTypeId;
            

            if(errors.length > 0){
                this.errors = errors;
                return;
            }

            this.$store.dispatch('addRisk', payload);
        }
    },
    computed: {
        riskTypes() {
            return this.$store.state.riskTypes;
        },
        getCurrentRiskTypeId () {
            let query = this.$route.query;
            if(query.riskTypeId && !this.riskTypeId){
                this.riskTypeId = parseInt(query.riskTypeId);
                this.showCancelBtn = true;
                this.showBackBtn = false;
                this.completeStep1();
            }
            
        }
    },
}
</script>