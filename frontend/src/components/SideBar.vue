<template>
<div class="row">
  <ul class="nav-container">
	<li class="nav-items" v-for="(category, index) in categories" :key="index">
		<div :class="`p${category}`" id="category" @click="onRoute(category)">
			{{ category }}
		</div>
		<div class="inner-item mt-4" v-if="category ==='Main'">
			<div :class="`p${mainCategory.pathName}`" id="product-name" v-for="(mainCategory, index) in mainCategories" :key="index" @click="onRoute(mainCategory.pathName)">{{ mainCategory.name }}</div>
		</div>
		<div class="inner-item mt-4" v-if="category ==='Product'">
			<div :class="`p${product.id}`" id="product-name" v-for="(product, index) in productCategories" :key="index" @click="onDetail(product.id)">
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

		}
  },
  props: ['categories', 'productCategories', 'mainCategories'],
	methods: {
		onRoute(name) {
			this.$router.push({name:name}, () => {})
		},
		onDetail(cid) {
			this.$router.push({name:'ProductItemMain', params:{cid: cid}}, () => {})
		},
		fixCategory () {
      document.querySelector('.p' + this.$route.matched[3].name).classList.add('active')
    },
	},
	watch: {
    '$route' (to, from) {
      document.querySelector('.p' + from.matched[3].name).classList.remove('active')
      document.querySelector('.p' + to.matched[3].name).classList.add('active')
    }
	},
	mounted() {
    this.fixCategory()
  },
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