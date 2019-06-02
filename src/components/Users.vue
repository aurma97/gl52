<template>
    <div class="container">
        <hr>
        <hr>
        <b-tabs position="is-centered" class="block">
            <b-tab-item label="Les utilisateurs">
                <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
                    <div >
                        <ul >
                            <li><router-link to="/">Accueil</router-link></li>
                            <li @click="isComponentModalActive = false; showUser == false"><router-link to="/users">Gestion des utilisateurs</router-link></li>
                            <li v-if="isComponentModalActive == true" class="is-active"><a href="#">Ajout d'un utilisateur</a></li>
                            <li v-if="showUser == true" class="is-active"><a href="#">modification d'un utilisateur</a></li>

                        </ul>                        
                    </div>
                    <hr>
                    <b-button
                        v-if="isComponentModalActive == false && showUser == false"
                        icon-left="plus" @click="isComponentModalActive = true">
                        Ajouter un utilisateur
                    </b-button>
                </nav>
               
            </b-tab-item>
        </b-tabs>
        <div class="column">
            <div class="has-text-right" v-if="isDelete">
                <span>
                    <button class="button is-danger" @click="deleteUser(idEqToDel)">Confirmation suppression</button>
                </span>
                &nbsp;
                <span>
                    <button class="button" @click="isDelete = false">Annuler</button>
                </span>
            </div>
        </div>
        
        <b-table 
                        v-if="isComponentModalActive == false && !showUser"
                        :data="isEmpty ? [] : this.$store.state.users.users"
                        :paginated="isPaginated"
                        :per-page="perPage"
                        :opened-detailed="defaultOpenedDetails"
                        ref="table"
                        detailed
                        detail-key="id"
                        @details-open="(row, index) => $toast.open(`Expanded ${row.username}`)"
                        :show-detail-icon="showDetailIcon"
                        :current-page.sync="currentPage"
                        :pagination-simple="isPaginationSimple"
                        :default-sort-direction="defaultSortDirection"
                        default-sort="name"
                        aria-next-label="Page suivante"
                        aria-previous-label="Page précedente"
                        aria-page-label="Page"
                        aria-current-label="Page actuelle">

                        <template slot-scope="props">
                            <b-table-column field="id" label="id" sortable>
                                <template v-if="showDetailIcon">
                                    {{ props.row.id }}
                                </template>
                                <template v-else>
                                    <a @click="toggle(props.row)">
                                        {{ props.row.id }}
                                    </a>
                                </template>
                            </b-table-column>
                            <b-table-column field="username" label="Username" sortable>
                                {{ props.row.username }}
                            </b-table-column>
                            <b-table-column field="first_name" label="Nom" sortable>
                                {{ props.row.first_name }}
                            </b-table-column>
                            <b-table-column field="last_name" label="Prénom" sortable>
                                {{ props.row.last_name }}
                            </b-table-column>
                            <b-table-column field="is_staff" label="métier" sortable centered>
                                <span class="tag">
                                    {{getPosition(props.row.is_staff,props.row.is_superuser)}}
                                </span>
                            </b-table-column>
                            <b-table-column field="date_joined" label="Date insertion" sortable centered>
                                <span class="tag is-success">
                                    {{ new Date(props.row.date_joined).toLocaleDateString() }}
                                </span>
                            </b-table-column>
                            


                            <b-table-column sortable centered>
                                <b-field grouped group-multiline>
                                    <div class="control is-flex">
                                        <button class="button is-warning" @click="getUser(props.row.id); showUser = true"><i class="fas fa-edit"></i></button>
                                    </div>
                                    <div>
                                        <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
                                    </div>
                                </b-field>
                            </b-table-column>
                        </template>

                        <template slot="detail" slot-scope="props">
                            <article class="media">
                                <div class="media-content">
                                    <div class="content">
                                        <p>
                                           <strong>{{ props.row.username }} - {{ props.row.last_name  }} {{props.row.first_name}}</strong>
                                            <br>
                                            <h4>permissons</h4>
                                            <ul>
                                                <li v-for="permission in props.row.user_permissions">
                                                    {{permission}}
                                                </li>
                                            </ul>
                                            
                                        </p>
                                    </div>
                                </div>
                            </article>
                        </template>

                        <!-- isEmpty -->
                        <template slot="empty">
                            <section class="section">
                                <div class="content has-text-grey has-text-centered">
                                    <p>
                                        <b-icon
                                            icon="emoticon-sad"
                                            size="is-large">
                                        </b-icon>
                                    </p>
                                    <p>Rien par ici.</p>
                                </div>
                            </section>
                        </template>
                    </b-table>
                    <!-- ajouter -->
                <template v-if="isComponentModalActive">
                    <section>
                        <div class="modal-card" style="width: auto">
                            <div>
                                <section class="modal-card-body">
                                    <b-field label="username">
                                        <b-input type="text" v-model="user.username" placeholder="username" required></b-input>
                                    </b-field>
                                    <b-field label="Prénom">
                                        <b-input v-model="user.first_name" placeholder="prénom"></b-input>
                                    </b-field>
                                    <b-field label="Nom">
                                        <b-input  v-model="user.last_name" placeholder="nom"></b-input>
                                    </b-field>
                                    <b-field label="Email">
                                        <b-input v-model="user.email" type="email">
                                        </b-input>
                                    </b-field>
                                    <b-field label="employé">
                                        <div class="block">
                                            <b-radio v-model="user.is_staff"
                                                native-value=true>
                                                oui
                                            </b-radio>
                                            <b-radio v-model="user.is_staff"
                                                native-value=false>
                                                non
                                            </b-radio>
                                        </div>   
                                    </b-field>
                                    <b-field v-if="user.is_staff == 'true'" label="admin">
                                        <div class="block">
                                            <b-radio v-model="user.is_superuser"
                                                native-value=true>
                                                oui
                                            </b-radio>
                                            <b-radio v-model="user.is_superuser"
                                                native-value=false>
                                                non
                                            </b-radio>
                                        </div>   
                                    </b-field>
                                    <b-field grouped group-multiline label="mot de passe">
                                         <div class="control is-flex">

                                        <b-input  v-model="user.password" placeholder="nom"></b-input>
                                         </div>
                                         <div class="control is-flex">

                                        <b-button type="is-primary" @click="generateRandomPassword">generate password</b-button>
                                         </div>                                        
                                    </b-field>
                                    
                                </section>
                                <footer class="modal-card-foot">
                                    <button class="button is-primary" @click="addUser">Valider</button>
                                    <b-button @click="isComponentModalActive = false">Annuler</b-button>
                                </footer>
                            </div>
                            <br>
                        </div>
                            
                    </section>
                </template>



                    <!-- modification -->
                <div class="notification" v-if="userOne && showUser" >
                    <h1 class="title is-2">Modification de " {{userOne.username}} " </h1>
                    
                    <div class="columns">
                        <div class="column">
                            <b-field label="username">
                                <b-input v-model="userOne.username"></b-input>
                            </b-field>
                            <b-field label="Prénom">
                                <b-input v-model="userOne.first_name" ></b-input>
                            </b-field>
                            <b-field label="Nom">
                                <b-input  v-model="userOne.last_name" ></b-input>
                            </b-field>
                            <b-field label="Email">
                                <b-input v-model="userOne.email" type="email">
                                </b-input>
                            </b-field>
                            <b-field label="employé">
                                <div class="block">
                                    <b-radio v-model="userOne.is_staff"
                                        native-value=true>
                                        oui
                                    </b-radio>
                                    <b-radio v-model="userOne.is_staff"
                                        native-value=false>
                                        non
                                    </b-radio>
                                </div>   
                            </b-field>
                            <b-field v-if="userOne.is_staff == 'true' || userOne.is_staff == true" label="admin">
                                <div class="block">
                                    <b-radio v-model="userOne.is_superuser"
                                        native-value=true>
                                        oui
                                    </b-radio>
                                    <b-radio v-model="userOne.is_superuser"
                                        native-value=false>
                                        non
                                    </b-radio>
                                </div>   
                            </b-field>
                            <b-field label="mot de passe">
                                        <div class="control is-flex">

                                            <b-input  v-model="userOne.password" placeholder="password"></b-input>
                                        </div>      
                                    </b-field>
                        </div>
                        
                            <b-field grouped group-multiline>
                                <div class="control is-flex">
                                    <b-button type="is-primary" @click="updateUser(userOne)">Modifier</b-button>
                                </div>
                            
                                <div class="control is-flex">
                                <b-button @click="showUser = false">Annuler</b-button>
                                </div>
                            </b-field>
                        </div>
                    </div>
                </div>

       
</template>

<script> 

import { mapState, mapActions } from 'vuex'

export default {
    computed:{
        users(){
            return this.$store.state.users;
        },
        userOne(){
            return this.$store.state.users.user
        },
    },
    methods:{
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        },
        randomPassword(length) {
            var chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+<>ABCDEFGHIJKLMNOP1234567890";
            var pass = "";
            for (var x = 0; x < length; x++) {
                var i = Math.floor(Math.random() * chars.length);
                pass += chars.charAt(i);
            }
            return pass;
        },
        generateRandomPassword() {
            this.user.password = this.randomPassword(15);
        },
        getPosition(is_staff,is_superuser){
            if(!is_staff){
                return "patient"
            }else if(is_staff && is_superuser){
                return "administrateur"
            }else {
                return "médecin"
            }
        },
        addUser(){
            // not working !!
            console.log(this.user);
            this.$store.dispatch('users/addUser', this.user)
            this.errors = this.$store.dispatch('users/getErrors')
            if(this.errors == 400 | this.errors == 500){
                this.$notification.open({
                    duration: 500,
                    message: `Un problème est survenu lors de l'ajout, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else{
                this.isLoading = true
                this.user = []
                setTimeout(() => {
                    this.$store.dispatch('users/getUsers');
                    this.$el.textContent
                    this.isLoading = false
                    this.showUser = false
                    this.isComponentModalActive = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Enregistrement effectué avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
        },
        deleteUser(payload){
            this.$store.dispatch('users/deleteUser', payload)
            this.isDelete = false
            this.errors = this.$store.dispatch('users/getErrors')
            console.log(this.errors)
            if(this.errors != 400 | this.erros != 500){
                setTimeout(() => {
                    this.$store.dispatch('users/getUsers');
                    //location.reload()
                    this.$el.textContent
                    this.isDelete = false
                    this.isLoading = false
                    this.showEquipment = false
                    this.isComponentModalActive = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Suppression effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
            else
            {
                this.$notification.open({
                    duration: 5000,
                    message: `Suppression impossible, l'équipement est utilisé par une réservation`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
        },
        getUser(payload){
            this.$store.dispatch('users/getUser', payload)
            this.user.id = this.userOne.id
            this.user.username = this.userOne.username
            this.user.first_name = this.userOne.first_name
            this.user.last_name = this.userOne.last_name
            this.user.is_staff = this.userOne.is_staff
            this.user.is_superuser = this.userOne.is_superuser
            this.user.password = this.userOne.password
            this.user.user_permissions = this.userOne.user_permissions
            this.user.groups = this.userOne.groups
            this.user.email = this.userOne.email
            this.user.last_login = this.userOne.last_login
            this.user.date_joined = this.userOne.date_joined
            this.user.is_active = this.userOne.is_active
            this.user.password = this.userOne.password
        },
        callDelete(id){
            this.idEqToDel = id
            this.isDelete = true
        },
        updateUser(payload){
            this.$store.dispatch('users/updateUser', payload)
            this.errors = this.$store.dispatch('users/getErrors');
            if(this.errors == 400 | this.errors == 500){
                this.$notification.open({
                    duration: 20000,
                    message: `Un problème est survenu lors de la mise à jour, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else
            {
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('users/getUsers');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.showUser = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Mise à jour effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)
                
            }
        }
    },
    data() {
        return {
            data:[],
            idEqToDel:'',
            isDelete: '',
            error: false, 
            isComponentModalActive : false,
            isEmpty: false,
            isPaginated: true,
            perPage: 5,
            defaultOpenedDetails: [1],
            showDetailIcon: true,
            currentPage: 1,
            showUser: false,
            isPaginationSimple: false,
            defaultSortDirection: 'asc',
            user:{
                id: '',
                password: "",
                last_login: null,
                is_superuser: false,
                username: "",
                first_name: "",
                last_name: "",
                email: "",
                is_staff: false,
                is_active: false,
                date_joined: null,
                groups: [],
                user_permissions: []
            }
        }
    }
    ,
    created() {
        this.$store.dispatch('users/getUsers');
    },
    test(){

    }
}

</script> 