//test.js
var util = require('../../utils/util.js')
Page({
  data: {
    datas: []
  },
  onLoad: function () {
    this.setData({
      datas: (wx.getStorageSync('logs') || []).map(function (log) {
        return util.formatTime(new Date(log))
      })
    })
  }
})
