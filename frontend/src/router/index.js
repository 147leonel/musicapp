import Vue from 'vue'
import VueRouter from 'vue-router'
import Music from '@/components/Music'

Vue.use(VueRouter)

const routes = [
  {
    path: '/musica/lista',
    name: 'Music',
    component: Music
  },
]

const router = new VueRouter({
  routes:routes,
  mode:'history',
})

export default router
