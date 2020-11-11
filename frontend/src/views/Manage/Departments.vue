<template>
  <div>
    <div>부서관리</div>
    <div>
      <input type="text" v-model="departmentName">
      <button type="button" class="btn btn-outline-primary" @click="makeDepartments()">부서 생성</button>
    </div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">부서명</th>
        </tr>
      </thead>
      <tbody>
        <tr class="departments" v-for="(department, index) in departments" :key="index">
          <th scope="row">{{ index + 1}}</th>
          <td>{{ department.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
export default {
  data() {
    return {
      departmentName : ''
    }
  },
  computed: {
    ...mapState('account', ['departments'])
  },
  methods: {
    ...mapActions('account', ['getDepartments', 'makeDepartment']),
    makeDepartments() {
      const departmentData = {
        name : this.departmentName
      }
      this.makeDepartment(departmentData)
      this.departmentName = ''
    }
  },
  created() {
    this.getDepartments()
  }
}
</script>

<style scoped>
.departments {
  cursor: pointer;
}

.departments:hover {
  background-color: #e9e9e9;
}

.table {
  text-align: center;
}
</style>