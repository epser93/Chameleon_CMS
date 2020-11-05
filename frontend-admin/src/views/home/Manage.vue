<template>
  <div class="row">
    <ul class="col-3 nav-container">
			<!-- <li class="nav-items">
				<div ref="User" @click="onRoute('User')">User</div>
			</li>
			<li class="nav-items">
				<div ref="UserLog" @click="onRoute('UserLog')">UserLog</div>
			</li> -->
			<!-- <li class="nav-items" v-for="(category, index) in categories" :key="index">
				<div :class="category" @click="onRoute(category)">{{ category }}</div>
			</li> -->
			<SideBar :categories="categories"></SideBar>
    </ul>
    <div class="col-9">
			<router-view></router-view>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'
export default {
	components: {
		SideBar
	},
	data() {
		return {
			categories : ["User", "Log"]
		}
	},
	methods: {
		onRoute(name) {
			this.$router.push({name:name}, () => {})
		},
		fixCategory () {
			for (let i=0; i<this.categories.length; i++) {
				let className = '.' + this.categories[i]
				if (this.$route.name === this.categories[i]) {
					document.querySelector(className).classList.add('active')
				} else {
					document.querySelector(className).classList.remove('active')
				}
			}
			// let category_list = [this.$refs.User, this.$refs.UserLog]
			// for (let i=0; i<category_list.length; i++) {
			// 	if (this.$route.name === category_list[i].innerHTML) {
			// 		category_list[i].classList.add('active')
			// 	} else {
			// 		category_list[i].classList.remove('active')
			// 	}
			// }
			// if (this.$route.name === 'User') {
			// 	this.$refs.UserLog.classList.remove('active')
			// 	this.$refs.User.classList.add('active')
			// } else {
			// 	this.$refs.User.classList.remove('active')
			// 	this.$refs.UserLog.classList.add('active')
			// }
		}
	},
	watch: {
		// '$route' (to, from) {
		// 	console.log(to)
		// 	console.log(from)
		// 	let category_list = [this.$refs.User, this.$refs.UserLog]
		// 	let before = null
		// 	let after = null
		// 	for (let i=0; i<category_list.length; i++) {
		// 		if (before !== null && after !== null) {
		// 			break
		// 		}
		// 		if (category_list[i].innerHTML === from.name) {
		// 			before = category_list[i]
		// 		} else if (category_list[i].innerHTML === to.name) {
		// 			after = category_list[i]
		// 		}
		// 	}
		// 	before.classList.remove('active')
		// 	after.classList.add('active')
		// }
		// '$route' : function() {
		// 	if (this.$route.name === 'User') {
		// 		this.$refs.UserLog.classList.remove('active')
		// 		this.$refs.User.classList.add('active')
		// 	} else {
		// 		this.$refs.User.classList.remove('active')
		// 		this.$refs.UserLog.classList.add('active')
		// 	}
		// },
		// '$route' : function() {
		// 	for (let i=0; i<this.categories.length; i++) {
		// 		let className = '.' + this.categories[i]
		// 		if (this.$route.name === this.categories[i]) {
		// 			document.querySelector(className).classList.add('active')
		// 		} else {
		// 			document.querySelector(className).classList.remove('active')
		// 		}
		// 	}
		// },

	},
	mounted() {
		// this.fixCategory()
	}
}
</script>

<style scoped>
.row {
	height: calc(100vh - 135px);
}

.nav-container {
	border-right: 1px gray solid;
	margin-bottom: 0;
}
</style>