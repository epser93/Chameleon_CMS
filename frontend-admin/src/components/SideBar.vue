<template>
<div class="row">
  <ul class="nav-container">
	<li class="nav-items" v-for="(category, index) in categories" :key="index">
		<div :class="category" id="category" @click="onRoute(category)">
			{{ category }}
		</div>
		<div class="inner-item mt-4" v-if="category ==='Product'">
			<div :class="product.name" id="product-name" v-for="(product, index) in productCategories" :key="index" @click="onDetail(product.id)">
			{{ product.name }}
			</div>
		</div>
	</li>
  </ul>
 </div>
</template>

<script>
export default {
  data() {
	return {
		cate : this.categories,
		productdCate : this.productCategories
	}
  },
  props: ['categories', 'productCategories'],
	methods: {
		onRoute(name) {
			this.$router.push({name:name}, () => {})
		},
		onDetail(cid) {
			console.log(cid)
			this.$router.push({name:'ProductItemMain', params:{cid: cid}}, () => {})
		},
		fixCategory () {
			for (let i=0; i<this.categories.length; i++) {
			let className = '.' + this.categories[i]
			let tmp = this.categories[i]
				if (this.$route.name.includes(tmp)) {
					if(tmp == 'Product'){
						this.InnerCategory()
					}
					else{
						this.OutCategory()
					}
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
		},

		InnerCategory () {
			for (let i=0; i<this.productCategories.length; i++) {
			let className = '.' + this.productCategories[i].name
			let tmp = this.productCategories[i].id

			if (this.$route.params.cid == tmp) {
				document.querySelector(className).classList.add('active')
			} else {
				document.querySelector(className).classList.remove('active')
			}
			}
		},
		OutCategory () {
			for (let i=0; i<this.productCategories.length; i++) {
			let className = '.' + this.productCategories[i].name
			document.querySelector(className).classList.remove('active')
			}
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
		'$route' : function() {
			// if('Main' in this.$route.name) {
			// 	let className = '.main'
			// 	document.querySelector(className).classList.add('active')
			// }
			for (let i=0; i<this.categories.length; i++) {
				let className = '.' + this.categories[i]
				let tmp = this.categories[i]
				if (this.$route.name.includes(tmp)) {

					document.querySelector(className).classList.add('active')
					if(tmp === 'Product'){
						this.InnerCategory()
					}
					else{
						this.OutCategory()
					}
				} else {
					document.querySelector(className).classList.remove('active')
				}
			}
		},

	},
	mounted() {
		this.fixCategory()
	}
}
</script>

<style scoped>
.nav-items {
	margin-top: 30px;
	margin-left: 50px;
	margin-bottom: 30px;
	font-size: 36px;
	list-style: none;
}

.nav-items div {
	text-decoration: none;
	color: black;
	position: relative;
	width: fit-content;
	cursor: pointer;
}

#product-name {
  margin-top: 10px;
  margin-left: 20px;
}

#product-name:hover::before {
	width: 100%;
}

#product-name::before {
	content: '';
	height: 5px;
	width: 0;
	background-color:#4ea1b5;
	border-radius: 10px;
	transition: 0.3s;
	position: absolute;
	bottom: -10px;
	left: 0;
}

#product-name.active::after {
	content: '';
	height: 5px;
	width: 100%;
	background-color: grey;
	border-radius: 10px;
	transition: 0.3s;
	position: absolute;
	bottom: -10px;
	left: 0;
}

.nav-items #category:hover::before {
	width: 100%;
}

.nav-items #category::before {
	content: '';
	height: 5px;
	width: 0;
	background-color: #4ea1b5;
	border-radius: 10px;
	transition: 0.3s;
	position: absolute;
	bottom: -10px;
	left: 0;
}

.nav-items #category.active::after {
	content: '';
	height: 5px;
	width: 100%;
	background-color: gray;
	border-radius: 10px;
	transition: 0.3s;
	position: absolute;
	bottom: -10px;
	left: 0;
}

.inner-item {
	font-size: 20px;
}
</style>