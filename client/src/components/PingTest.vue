<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'PingTest',
  data() {
    return {
      msg: 'Ping received!',
    };
  },
};
</script>
