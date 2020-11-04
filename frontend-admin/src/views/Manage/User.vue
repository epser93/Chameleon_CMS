<template>
  <div class="container-fluid">
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">부서</th>
            <th scope="col">이름</th>
            <th scope="col">아이디</th>
            <th scope="col">권한</th>
          </tr>
        </thead>
        <tbody>
          <tr class="user-infos" @click="console(userinfo)" v-for="(userinfo, idx) in userinfos" :key="idx">
            <th scope="row">{{ idx+1 }} </th>
            <td>{{ userinfo.department }}</td>
            <td>{{ userinfo.name }}</td>
            <td>{{ userinfo.id }}</td>
            <td>{{ sliceAuthorities(userinfo.authority) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <AuthorityModal :modalinfos="modalinfos"></AuthorityModal>
  </div>
</template>

<script>
import AuthorityModal from '@/components/AuthorityModal'
import $ from 'jquery'
export default {
  components: {
    AuthorityModal
  },
  data() {
    return {
      modalinfos : [],
      userinfos: [
        {
          department: "생산관리",
          name : "송은석",
          id : "id1",
          authority: ["Product"]
        },
        {
          department: "품질관리",
          name : "강현영",
          id : "id2",
          authority : ["Main+Notice"]
        },
        {
          department: "구매",
          name : "장주환",
          id : "id3",
          authority : ["Product"]
        },
        {
          department: "전산",
          name : "김유기",
          id : "id4",
          authority : ["Product"]
        },
        {
          department: "마케팅",
          name : "임선빈",
          id : "id5",
          authority : ["Event"]
        },
        {
          department: "개발",
          name : "윤상목",
          id : "id6",
          authority : ["Main+Notice", "Event"]
        }
      ]
    }
  },
  methods: {
    console(userinfo) {
      console.log(userinfo)
      this.modalinfos = userinfo
      $('#authorityModal').modal('show')
    },

    sliceAuthorities(authorities) {
      let authoritiyList = ""
      for (let i=0; i<authorities.length; i++) {
        if (i === authorities.length - 1) {
          authoritiyList += authorities[i]
        } else {
          authoritiyList += authorities[i] + ', '
        }
      }
      return authoritiyList
    }
  }

}
</script>

<style scoped>
.table-container {
  width: 100%;
  margin-top: 10vh; 
  text-align: center;
}

.user-infos {
  cursor: pointer;
}

.user-infos:hover {
  background-color: #e9e9e9;
}
</style>