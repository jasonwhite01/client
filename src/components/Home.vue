<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Member</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Member</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Email</th>
              <th scope="col">Address</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(rs, index) in members" :key="index">
              <td>{{ rs.name }}</td>
              <td>{{ rs.email }}</td>
              <td>{{ rs.address }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
 
export default {
  name: 'Home-Home',
  data() {
    return {
      members: [],
    };
  },
  methods: {
    getMembers() {
      const path = 'http://localhost:5000/members';
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.members = res.data.members;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMembers();
  },
};
</script>
