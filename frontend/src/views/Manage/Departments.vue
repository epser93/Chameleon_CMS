<template>
  <div class="container">
    <div class="table-container mt-0">
      <div class="d-flex align-items-center justify-content-between">
        <h5 class="mb-0">부서 관리</h5>
        <div class="input-group mb-3 mt-3">
          <input type="text" v-model="departmentName" class="form-control" placeholder="부서명을 입력하세요." aria-label="Recipient's username" aria-describedby="button-addon2">
          <div class="input-group-append">
            <button @click="makeDepartments()" class="btn btn-secondary" type="button" id="button-addon2">부서 생성</button>
          </div>
        </div>
      </div>
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
.input-group {
  float: right;
  width: 40%;
}

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