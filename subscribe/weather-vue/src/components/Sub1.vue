<template>
  <div class="sub" v-html="buff">
  </div>
</template>

<script>
export default {
  data () {
    return {
      buff: 'Sub1:<br>'
    }
  },
  mqtt: {
    /** 'VueMqtt/publish1' or '+/publish1' */
    'VueMqtt/testtopic/1' (data) {
      this.buff = this.buff + data + '<br>'
    }
  }
}
</script>
