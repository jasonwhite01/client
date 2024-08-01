<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br><br>
        <h1>News Feed Podcasts</h1>
        <hr><br><br>
        <table class="table table-hover">
          <tbody>
            <tr v-for="(rs, index) in feeds" :key="index">
              <td>
                <h3>{{ rs.title }}</h3>
                <p><span v-html="rs.description"></span></p>
                <p><a :href = "rs.podcasturl"><img src="../assets/podcast.png" alt="Girl in a jacket" width="30" height="20"/></a></p>
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
  name: 'NewsFeed',
  data() {
    return {
      feeds: [],
    };
  },
  methods: {
    getFeeds() {
      const path = 'http://localhost:5000/feeds';
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.feeds = res.data.members;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getFeeds();
  },
};
</script>
