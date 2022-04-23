<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tweets</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Connect Account</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Text</th>
              <th scope="col">ID</th>
              <th scope="col">Likes</th>
              <th scope="col">Retweets</th>
              <th scope="col">Replies</th>
              <th scope="col">Quotes</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(tweet,index) in tweets" :key="index">
              <td>{{ tweet.text }}</td>
              <td>{{ tweet.id }}</td>
              <td>{{ tweet.like_count }}</td>
              <td>{{ tweet.retweet_count }}</td>
              <td>{{ tweet.reply_count }}</td>
              <td>{{ tweet.quote_count }}</td>
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
  data() {
    return {
      tweets: [],
    };
  },
  methods: {
    getTweets() {
      const path = 'http://localhost:5050/public_tweets';
      axios.get(path)
        .then((res) => {
          this.tweets = res.data.tweets;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTweets();
  },
};
</script>