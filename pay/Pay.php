<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2017/7/27
 * Time: 9:32
 */

namespace app\member\controller;


use app\common\MemberBase;

class Pay extends MemberBase
{
    private function valid($code = 0, $fee = 0)
    {
        if (
            empty($code) ||
            empty($fee)
        ) {
            $this->error("非法访问", "/");
        }
    }

    public function do_alipay($code, $fee)
    {
        $this->valid($code, $fee);
        common_vendor('Alipay.Corefunction');
        common_vendor('Alipay.Md5function');
        common_vendor('Alipay.Notify');
        common_vendor('Alipay.Submit');
        $alipay_config = array(
            'partner' => config('alipay_partner'),   //这里是你在成功申请支付宝接口后获取到的PID；
            'key' => config('alipay_key'),//这里是你在成功申请支付宝接口后获取到的Key
            'private_key_path' => 'key/rsa_private_key.pem',
            'ali_public_key_path' => 'key/alipay_public_key.pem',
            'sign_type' => strtoupper('MD5'),
            'input_charset' => 'utf-8',
            'cacert' => getcwd() . '\\cacert.pem',
            'transport' => 'http',
        );
        /**
         * 支付成功跳转路径
         */
        $return_url = config('site_url') . url('/myorder'); //页面跳转同步通知页面路径
        //页面跳转同步通知页面路径
        $call_back_url = config('site_url') . url('/myorder'); //页面跳转同步通知页面路径
        //需http://格式的完整路径，不允许加?id=123这类自定义参数
        $notify_url = sprintf("%s/%s/code/%s",
            config('site_url'),
            "member/pay/alipay_notify",
            $code); //服务器异步通知页面路径

        $payment_type = "1"; //支付类型 //必填，不能修改
        $seller_email = config('alipay_seller_email');//卖家支付宝帐户必填
        $out_trade_no = $code;//商户订单号 通过支付页面的表单进行传递，注意要唯一！
        $subject = "对" . $code . '交易号付款';  //订单名称 //必填 通过支付页面的表单进行传递
        $total_fee = $fee;   //付款金额  //必填 通过支付页面的表单进行传递
        $body = '订单付款';
        $anti_phishing_key = "";//防钓鱼时间戳 //若要使用请调用类文件submit中的query_timestamp函数
        $user_IP = isset($_SERVER["HTTP_VIA"]) ? $_SERVER["HTTP_X_FORWARDED_FOR"] : $_SERVER["REMOTE_ADDR"];
        $user_IP = isset($user_IP) ? $user_IP : $_SERVER["REMOTE_ADDR"];
        $exter_invoke_ip = $user_IP; //客户端的IP地址
        /************************************************************/
        $extra_common_param = '1010101';//test
        //构造要请求的参数数组，无需改动
        $parameter = array(
            "service" => "create_direct_pay_by_user",
            "partner" => trim(config('alipay_partner')),
            "payment_type" => $payment_type,
            "notify_url" => $notify_url,
            "return_url" => $return_url,
            "seller_email" => $seller_email,
            "out_trade_no" => $out_trade_no,
            "subject" => $subject,
            "total_fee" => $total_fee,
            "body" => $body,
            "extra_common_param" => $extra_common_param,
            "anti_phishing_key" => $anti_phishing_key,
            "exter_invoke_ip" => $exter_invoke_ip,
            "_input_charset" => trim(strtolower($alipay_config['input_charset']))
        );
        //建立请求
        /** @var  \AlipaySubmit $alipaySubmit */
        $alipaySubmit = new \AlipaySubmit($alipay_config);
        $html_text = $alipaySubmit->buildRequestForm($parameter, "post", "确认");
        echo $html_text;
    }

    public function alipay_notify($code)
    {
        common_vendor('Alipay.Corefunction');
        common_vendor('Alipay.Md5function');
        common_vendor('Alipay.Notify');
        common_vendor('Alipay.Submit');
        //这里我们通过TP的C函数把配置项参数读出，赋给$alipay_config；
        $alipay_config = array(
            'partner' => config('alipay_partner'),   //这里是你在成功申请支付宝接口后获取到的PID；
            'key' => config('alipay_key'),//这里是你在成功申请支付宝接口后获取到的Key
            'private_key_path' => 'key/rsa_private_key.pem',
            'ali_public_key_path' => 'key/alipay_public_key.pem',
            'sign_type' => strtoupper('MD5'),
            'input_charset' => 'utf-8',
            'cacert' => getcwd() . '\\cacert.pem',
            'transport' => 'http',
        );

        $alipayNotify = new \AlipayNotify($alipay_config);
        $verify_result = $alipayNotify->verifyNotify();


        if ($verify_result) {
            //验证成功
            //获取支付宝的通知返回参数，可参考技术文档中服务器异步通知参数列表
            $out_trade_no = $_POST['out_trade_no'];      //商户订单号
            $extra_common_param = $_POST['extra_common_param'];
            $trade_no = $_POST['trade_no'];          //支付宝交易号
            $trade_status = $_POST['trade_status'];      //交易状态
            $total_fee = $_POST['total_fee'];         //交易金额
            $notify_id = $_POST['notify_id'];         //通知校验ID。
            $notify_time = $_POST['notify_time'];       //通知的发送时间。格式为yyyy-MM-dd HH:mm:ss。
            $buyer_email = $_POST['buyer_email'];       //买家支付宝帐号；
            $parameter = array(
                "out_trade_no" => $out_trade_no, //商户订单编号；
                "trade_no" => $trade_no,     //支付宝交易号；
                "total_fee" => $total_fee,    //交易金额；
                "trade_status" => $trade_status, //交易状态
                "extra_common_param" => $extra_common_param,
                "notify_id" => $notify_id,    //通知校验ID。
                "notify_time" => $notify_time,  //通知的发送时间。
                "buyer_email" => $buyer_email,  //买家支付宝帐号；
            );
            $re = true;
            if ($_POST['trade_status'] == 'TRADE_FINISHED') {
                $re = true;
            } else if ($_POST['trade_status'] == 'TRADE_SUCCESS') {
                //买家支付成功，开始修改订单的支付方式和付款状态
                #todo 支付成功后的处理
                //$code
            }
            if ($re) {
                echo "success";
            }
        } else {
            //验证失败
            echo "fail" . $_SESSION['master']['mas_id'];
        }
    }

    public function do_weixin($code, $fee = 1)
    {
        $this->valid($code, $fee);
        common_vendor('WxPayPubHelper.WxPaypubconfig');
        common_vendor('WxPayPubHelper.SDKRuntimeException');
        common_vendor('WxPayPubHelper.WxPayPubHelper');
        common_vendor('phpqrcode.qrlib');
        $fee = $fee * 100;
        //使用统一支付接口
        $unifiedOrder = new \UnifiedOrder_pub();
        $out_trade_no = $code;
        $unifiedOrder->setParameter("body", "订单付款");//商品描述
        $unifiedOrder->setParameter("out_trade_no", "$out_trade_no");//商户订单号
        $unifiedOrder->setParameter("total_fee", $fee);//总金额
        $unifiedOrder->setParameter("notify_url",
            sprintf("%s/%s/code/%s",
                config('site_url'),
                "member/pay/weixin_notifyurl",
                $code)
        );//通知地址
        $unifiedOrder->setParameter("trade_type", "NATIVE");//交易类型
        //非必填参数，商户可根据实际情况选填
        //获取统一支付接口结果
        $unifiedOrderResult = $unifiedOrder->getResult();
        $code_url = '';
        //print_r($unifiedOrderResult);
        //商户根据实际情况设置相应的处理流程
        if ($unifiedOrderResult["return_code"] == "FAIL") {
            //商户自行增加处理流程
            return json([
                "code" => 1000,
                "qrcode" => "通信出错：" . $unifiedOrderResult['return_msg']
            ]);
        } elseif ($unifiedOrderResult["result_code"] == "FAIL") {
            //商户自行增加处理流程
            return json([
                "code" => 1000,
                "qrcode" => "错误代码：" . $unifiedOrderResult['err_code'] . "<br>" + "错误代码描述：" . $unifiedOrderResult['err_code_des']
            ]);
        } elseif ($unifiedOrderResult["code_url"] != NULL) {
            // 从统一支付接口获取到code_url
            $code_url = $unifiedOrderResult["code_url"];
            // 商户自行增加处理流程
            //
        }
        return response(\QRcode::png($code_url), 200)->contentType("image/jpg");
    }

    /**
     * @param $code
     *  服务器异步通知页面方法
     * 其实这里就是将notify_url.php文件中的代码复制过来进行处理
     */
    public function weixin_notifyurl($code)
    {
        vendor('WxPayPubHelper.SDKRuntimeException');
        vendor('WxPayPubHelper.WxPayPubHelper');
        //使用通用通知接口
        $notify = new \Notify_pub();

        //存储微信的回调
        $xml = $GLOBALS['HTTP_RAW_POST_DATA'];
        $notify->saveData($xml);

        //验证签名，并回应微信。
        //对后台通知交互时，如果微信收到商户的应答不是成功或超时，微信认为通知失败，
        //微信会通过一定的策略（如30分钟共8次）定期重新发起通知，
        //尽可能提高通知的成功率，但微信不保证通知最终能成功。
        if ($notify->checkSign() == FALSE) {
            $notify->setReturnParameter("return_code", "FAIL");//返回状态码
            $notify->setReturnParameter("return_msg", "签名失败");//返回信息
        } else {
            $notify->setReturnParameter("return_code", "SUCCESS");//设置返回码
        }
        $returnXml = $notify->returnXml();
        echo $returnXml;

        //==商户根据实际情况设置相应的处理流程，此处仅作举例=======
        //$log_name="notify_url.log";//log文件路径
        //$this->log_result($log_name,"【接收到的notify通知】:\n".$xml."\n");

        if ($notify->checkSign() == TRUE) {
            if ($notify->data["return_code"] == "FAIL") {
                //此处应该更新一下订单状态，商户自行增删操作
                //$this->log_result($log_name,"【通信出错】:\n".$xml."\n");
            } elseif ($notify->data["result_code"] == "FAIL") {
                //此处应该更新一下订单状态，商户自行增删操作
                //$this->log_result($log_name,"【业务出错】:\n".$xml."\n");
            } else {
                //此处应该更新一下订单状态，商户自行增删操作
                //买家支付成功，开始修改订单的支付方式和付款状态
                //$this->log_result($log_name,$out_trade_no."【支付成功0000】:\n".$xml."\n");
                if ($notify->data["attach"]) {
                    //$code
                    #todo 充值成功
                } else {
                    #todo 订单支付成功成功
                }
            }
            echo "success";
        }
    }

    //查询订单的支付状态
    public function order_query_from_weixin($code)
    {
        #todo 获取订单是否支付成功
    }

    /**
     * 银联支付
     * @param $code
     * @param $fee
     */
    public function do_unionpay($code, $fee)
    {
        $this->valid($code, $fee);
        define('SDK_SIGN_CERT_PATH', config('SDK_SIGN_CERT_PATH'));
        define('SDK_ENCRYPT_CERT_PATH', config('SDK_ENCRYPT_CERT_PATH'));
        define('SDK_VERIFY_CERT_DIR', config('SDK_VERIFY_CERT_DIR'));
        define('SDK_SIGN_CERT_PWD', config('SDK_SIGN_CERT_PWD'));
        define("SDK_FRONT_NOTIFY_URL", config('site_url') . url('/myorder'));
        //后台通知地址
        define("SDK_BACK_NOTIFY_URL", sprintf("%s/%s/code/%s",
            config('site_url'),
            'member/pay/unionpay_notify',
            $code
        ));
        common_vendor('Unionpay.sdk.acp_service');
        /**************************请求参数**************************/
        header('Content-type:text/html;charset=utf-8');
        $order_no = $code;
        $params = array(
            //以下信息非特殊情况不需要改动
            'version' => '5.0.0',                 //版本号
            'encoding' => 'utf-8',                  //编码方式
            'txnType' => '01',                      //交易类型
            'txnSubType' => '01',                  //交易子类
            'bizType' => '000201',                  //业务类型
            'frontUrl' => \com\unionpay\acp\sdk\SDK_FRONT_NOTIFY_URL,  //前台通知地址
            'backUrl' => \com\unionpay\acp\sdk\SDK_BACK_NOTIFY_URL,      //后台通知地址
            'signMethod' => '01',                  //签名方法
            'channelType' => '08',                  //渠道类型，07-PC，08-手机
            'accessType' => '0',                  //接入类型
            'currencyCode' => '156',              //交易币种，境内商户固定156

            //TODO 以下信息需要填写
            'merId' => config('merId'),        //商户代码，请改自己的测试商户号
            'orderId' => $order_no,    //商户订单号
            'txnTime' => date('YmdHis'),        //订单发送时间，格式为YYYYMMDDhhmmss，取北京时间，此处默认取demo演示页面传递的参数
            'txnAmt' => $fee * 100,    //交易金额，单位分，此处默认取demo演示页面传递的参数
            // 		'reqReserved' =>'透传信息',        //请求方保留域，透传字段，查询、通知、对账文件中均会原样出现，如有需要请启用并修改自己希望透传的数据

            //TODO 其他特殊用法请查看 special_use_purchase.php
        );

        \com\unionpay\acp\sdk\AcpService::sign($params);
        $uri = \com\unionpay\acp\sdk\SDK_FRONT_TRANS_URL;
        $html_form = \com\unionpay\acp\sdk\AcpService::createAutoFormHtml($params, $uri);
        echo $html_form;
    }

    /******************************
     * 银联支付的异步接收
     *******************************/
    public function unionpay_notify($code)
    {
        define('SDK_SIGN_CERT_PWD', config('SDK_SIGN_CERT_PWD'));
        define("SDK_FRONT_NOTIFY_URL", config('site_url') . url('User/order'));
        //后台通知地址
        define("SDK_BACK_NOTIFY_URL", config('site_url') . '/index.php/Unionpay/notifyurl/payid/' . input('get.payid') . '/type/' . input('get.type'));

        common_vendor('Unionpay.sdk.acp_service');
        if (isset ($_POST ['signature'])) {
            echo \com\unionpay\acp\sdk\AcpService::validate($_POST) ? '验签成功' : '验签失败';
            $out_trade_no = $_POST ['orderId']; //其他字段也可用类似方式获取
            $total_fee = $_POST ['txnAmt'] / 100;
            $respCode = $_POST ['respCode']; //判断respCode=00或A6即可认为交易成功
            if ($respCode == '00' || $respCode == 'A6') {

                //买家支付成功，开始修改订单的支付方式和付款状态
                //$code @todo 订单操作
                echo "success";        //请不要修改或删除
            }
        } else {
            echo '签名为空';
        }
    }
}