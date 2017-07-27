<h4>----------请求报文-------------------</h4>
<h4>1. PC端商户界面点击银行网银图标直接跳转到银行网银支付</h4>
<p class="faq">
【仅适用PC端网页支付】<br>
（因测试环境所有商户号都默认不允许开通网银支付权限，所以要实现此功能需要使用正式申请的商户号去生产环境测试）：<br>
  1）联系银联业务运营部门开通商户号的网银前置权限<br>
  2）上送issInsCode字段，该字段的值参考《平台接入接口规范-第5部分-附录》（全渠道平台银行名称-简码对照表）<br>
  'issInsCode' => 'ABC',  //发卡机构代码<br>
</p>

<h4>2. 支付商户直接上送卡号并在银联页面锁定该卡号支付：</h4>
<p class="faq">
  【适用PC端网页】<br>
  需上送accNo，reserved这个2个字段（仅送accNo时会默认填上这个卡号，但用户仍能修改卡，必须送保留域用法防止修改）<br>
  'accNo' => '6221558812340000',  //需锁定的卡号<br>
  'reserved' => '{cardNumberLock=1}',    //银联定义的系统保留域，锁定卡号，值不能修改<br>
  【使用wap支付】<br>
   上送accNo即可，持卡人不能修改卡号<br>
</p>

<h4>3. 网关消费支付分期付款实现：</h4>
<p class="faq">
【适用PC端网页，wap支付】<br>
  1）联系银联业务运营部门申请开通商户号的分期付款权限<br>
  2）请求报文txnSubType送03<br>
  <span style="width:2em;"></span>'txnSubType' => '03',                //分期付款<br>
  3）测试环境使用测试卡号6221558812340000做金额介于10-1000之间金额的消费交易测试<br>
</p>

<h4>4. 网关支付成功后，自动跳转到商户网站：</h4>
<p class="faq">
【适用PC端网页，wap支付】<br>
联系银联业务运营部门开通商户号的自动跳转功能。<br>
</p>

<h4>5. 透传字段</h4>
<p class="faq">
【适用PC端网页，wap支付】<br>
  'reqReserved' =>'透传信息', //请求方保留域，透传字段，查询、通知、对账文件中均会原样出现，如有需要请启用并修改自 己希望透传的数据<br>
</p>

<h4>-------------通知报文---------------------</h4>
<h4>6. 返回报文中返回卡号，卡类型，支付方式:</h4>
<p class="faq">
【适用PC端网页，wap支付】<br>
需在申请入网或者已经入网后给银联业务运营中心申请开通这3种权限<br>

</p>
