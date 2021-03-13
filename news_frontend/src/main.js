// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from "element-ui";
import 'element-ui/lib/theme-chalk/index.css';
import App from './App'
import router from './router'
import axios from "axios";
import moment from 'moment';

Vue.config.productionTip = false;
//axios 发送请求
Vue.prototype.$axios = axios;
axios.defaults.baseURL = 'http://127.0.0.1:8090/newsapi';
//moment 处理时间
Vue.prototype.$moment = moment;
moment.locale('zh-cn');

Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
