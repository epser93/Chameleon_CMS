<template>
	<div class="container-fluid">
		<div class="row">
			<ul class="col-3 nav-container p-0 align-items-start">
					<SideBar :categories="categories"></SideBar>
			</ul>
			<div class="col-9 p-0">
				<router-view></router-view>
			</div>
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
			categories : ["Departments", "User", "Log"]
		}
	}
}
</script>

<style scoped>
.row {
	height: calc(100vh - 135px);
}

.nav-container {
	border-right: 8px #eeeeee solid;
	margin-bottom: 0;
	height: calc(100vh - 115px);
}
</style>