<template>
    <header>
        <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="container">
                <nav class="navbar is-link is-bold is-fixed-top has-shadow" role="navigation" aria-label="main navigation">
            <div id="vue-app" class="container">
                <div class="navbar-brand">
                    <router-link to="/">
                        <img src="https://www.utbm.fr/wp-content/uploads/2015/04/logo_utbm.png" width="170" height=700 alt="Menu">
                    </router-link>
                    <div @click="active = !active" class="navbar-burger burger" data-target="navMenu">
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                    </div>
                </div>

                <div id="navMenu" class="navbar-menu" v-bind:class="{'is-active': active}">
                    <div class="navbar-start">
                        <div class="navbar-item">
                            <h3 class="title is-5" style="color:white">Gest Equip</h3>    
                        </div>
                    </div>
                    <div class="navbar-end">
                        <router-link class="navbar-item" to="/equipements" exact>
                            <i class="fas fa-medkit"></i>&nbsp;&nbsp;Equipements
                        </router-link>
                        <router-link class="navbar-item" to="/permissions" exact>
                            <i class="fas fa-shield-alt"></i>&nbsp;&nbsp;Permissions
                        </router-link>
                        <router-link class="navbar-item" to="/reservation" exact>
                            <i class="fas fa-concierge-bell"></i>&nbsp;&nbsp;Reservation
                        </router-link>
                        <router-link class="navbar-item" to="/support" exact>
                            <i class="fas fa-life-ring"></i>&nbsp;&nbsp;Support
                        </router-link>

                        <!-- <router-link class="navbar-item" to="/connexion">
                            <i class="fas fa-sign-in-alt"></i>&nbsp;&nbsp;Connexion
                        </router-link>
                        <router-link class="navbar-item" to="/inscription">
                            <i class="fas fa-file-alt"></i>&nbsp;&nbsp;Inscription
                        </router-link> -->
                        <div class="navbar-item has-dropdown is-hoverable" >
                            <a class="navbar-link">
                                Bonjour {{username}}
                            </a>
                            <div class="navbar-dropdown">
                                <router-link class="navbar-item" to="/mon-compte" exact>
                                    <i class="fas fa-user-circle"></i>&nbsp;&nbsp;Mon compte
                                </router-link>
                                <div class="navbar-divider"></div>
                                <span class="navbar-item">
                                    <a class="button is-link is-inverted" exact>
                                        <span class="icon">
                                        <i class="fas fa-sign-out-alt "></i>
                                        </span>
                                        <span>Déconnexion</span>
                                    </a>
                                </span>
                            </div>
                        </div>
                    </div>     
                </div>
            </div>
        </nav>
        <hr>
        </div>
        </nav>
  
    </header>
</template>

<script>

export default {
    data(){
        return{
            active: false,
            username: 'Marcel'
        }
    },
    computed : {

    },
    created(){
    },
    mounted(){
     
    },
    methods: {
    
    }
}
</script>