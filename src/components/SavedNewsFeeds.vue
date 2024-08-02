<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br><br>
        <h1>Saved News Feed Podcasts</h1>
        <hr><br><br>
        <table class="table table-hover">
          <tbody>
            <tr v-for="(rs, index) in feeds" :key="index">
              <td>
                <h3>{{ rs.feed_headline }}</h3>
                <p><span v-html="rs.feed_description"></span></p>
                <p><a :href = "rs.feed_podcasturl"><img src="../assets/podcast.png" alt="Girl in a jacket" width="30" height="20"/></a></p>
              </td>
              <!-- <td><button @click='saveFeed(rs.title, rs.description, rs.podcasturl)'>Save</button></td> -->
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
    getSavedFeeds() {
      const path = 'http://localhost:5000/feeds/savedfeeds';
      console.log('in getSavedFeeds()')
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.feeds = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    unsaveFeed(feed_title, feed_description, feed_podcasturl){
      axios({
        baseURL: 'http://localhost:5000',
        url: '/feeds',
        method: 'delete',
        data: {
          title: feed_title,
          description: feed_description,
          podcasturl: feed_podcasturl
        }
      }).then(res=>{
              console.log(res);
      }).catch(err=>{
          console.log(err);
      })
    }
  },
  created() {
    this.getSavedFeeds();
  },
};
</script>
