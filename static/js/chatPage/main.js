// variables
let userName = null;
let state = "SUCCESS";

// functions
function Message(arg) {
  this.text = arg.text;
  this.message_side = arg.message_side;

  this.draw = (function (_this) {
    return function () {
      let $message;
      $message = $($(".message_template").clone().html());
      $message.addClass(_this.message_side).find(".text").html(_this.text);
      $(".messages").append($message);

      return setTimeout(function () {
        return $message.addClass("appeared");
      }, 0);
    };
  })(this);
  return this;
}

function makebutton(message_side, location, date) {
  let $message;
  let html = "";
  alert(location, date);
  let butname = ["휴업", "요양", "장해"];
  //파라메타 변수 전송시 작은따옴표 체크
  for (let i = 0; i < 3; i++) {
    html += `<button onclick='f1(${location},${date},"${butname[i]}")'></button>`;
  }
  alert(html);
  //
  //<button onclick='f1([object Object], 휴업)'></button>
  //<button onclick='f1([object Object], 요양)'></button>
  //<button onclick='f1([object Object], 장해)'></button>

  $message = $($(".message_template").clone().html());
  $message.addClass(message_side).find(".text_wrapper").html(html);
  $(".messages").append($message);

  return setTimeout(function () {
    return $message.addClass("appeared");
  }, 0);
}

function f1(eloc, eacc, name) {
  let button = " ";

  let loc = eloc;
  let acc = eacc;
  //let injury=data['injury'];
  alert("엔티팉는" + loc + acc + "입니다.");
  //window.open('#탬플릿주소 /loc/acc/button/button','new window');
}
function getMessageText() {
  let $message_input;
  $message_input = $(".message_input");
  return $message_input.val();
}

function sendMessage(text, message_side) {
  let $messages, message;
  $(".message_input").val("");
  $messages = $(".messages");
  message = new Message({
    text: text,
    message_side: message_side,
  });
  message.draw();

  $messages.animate({ scrollTop: $messages.prop("scrollHeight") }, 300);
}

function greet() {
  setTimeout(function () {
    return sendMessage("Lobot demo에 오신걸 환영합니다.", "left");
  }, 1000);

  setTimeout(function () {
    return sendMessage("사용할 닉네임을 알려주세요.", "left");
  }, 2000);
}

function onClickAsEnter(e) {
  if (e.keyCode === 13) {
    onSendButtonClicked();
  }
}


function callApi(loc, acc, injury) {

    var form = document.createElement("form");
    form.setAttribute("charset", "UTF-8");
    form.setAttribute("method", "Post"); // Get 또는 Post 입력
    form.setAttribute("action", "http://127.0.0.1:8000/judgement/call/");


    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "button");
    hiddenField.setAttribute("value", "요양"); // 바꿀꺼
    form.appendChild(hiddenField);

    hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "acc");
    hiddenField.setAttribute("value", "추락"); //바꿀꺼
    form.appendChild(hiddenField);

    hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "loc");
    hiddenField.setAttribute("value", '현장'); // 바꿀꺼
    form.appendChild(hiddenField);

    document.body.appendChild(form);
    form.submit();

    }

function setUserName(username) {
  if (username != null && username.replace(" ", "" !== "")) {
    setTimeout(function () {
      return sendMessage(
        "반갑습니다." + username + "님. 닉네임이 설정되었습니다.",
        "left"
      );
    }, 1000);
    setTimeout(function () {
      return sendMessage("어떤 판결문에 대해 궁금하신가요?>_<", "left");
    }, 2000);
    return username;
  } else {
    setTimeout(function () {
      return sendMessage("올바른 닉네임을 이용해주세요.", "left");
    }, 1000);

    return null;
  }
}

function requestChat(messageText, url_pattern) {
    alert(url_pattern)
    alert(userName)
    alert(messageText)
  $.ajax({
    url:
      "http://127.0.0.1:5500/" + url_pattern + "/" + userName + "/" + messageText,
    type: "GET",
    dataType: "json",
    success: function (data) {
        callApi(data['answer']['LOC'] ,data['answer']['ACC'], data['answer']['INJURY'])
//            state = data['state'];
//
//            if (state === 'SUCCESS') {
//              answer=data['answer']['LOC']+"에서"+data['answer']['ACC']+"사고로 인해"+ data['answer']['INJURY']+"부상을 당하셨군요"
//
//                sendMessage(answer, 'left');
//                callApi(data['answer']['LOC'] ,data['answer']['ACC'], data['answer']['INJURY'])
//                makebutton('left',data['answer']['LOC'],data['answer']['ACC'])
//            } else if (state === 'REQUIRE_LOC') {
//                return sendMessage('어디장소에서 사고가 났나요?(출근중,회사에서,현장에서 등)', 'left');
//            }else if (state === 'REQUIRE_ACC') {
//                return sendMessage('무슨 사고가 있으셨나요?', 'left');
//            }else if (state === 'REQUIRE_INJURY') {
//                return sendMessage('어 부상을 입으셨나요?', 'left');
//            } else if (state === 'REQUIRE_CHECK') {
//                return sendMessage('중복된 정보입니다.이전 질문에 답변 부탁드립니다.', 'left');
//            } else {
//                return sendMessage('죄송합니다. 무슨말인지 잘 모르겠어요.', 'left');
//            }
        },

        error: function (request, status, error) {
            console.log(error);

            return sendMessage('죄송합니다. 서버 연결에 실패했습니다.', 'left');
        }
    });
}

function onSendButtonClicked() {
  let messageText = getMessageText();
  sendMessage(messageText, "right");

  if (userName == null) {
    userName = setUserName(messageText);
  } else {
    if (messageText.includes("안녕")) {
      setTimeout(function () {
        return sendMessage("안녕하세요. 저는 Kochat 여행봇입니다.", "left");
      }, 1000);
    } else if (messageText.includes("고마워")) {
      setTimeout(function () {
        return sendMessage("천만에요. 더 물어보실 건 없나요?", "left");
      }, 1000);
    } else if (messageText.includes("없어")) {
      setTimeout(function () {
        return sendMessage("그렇군요. 알겠습니다!", "left");
      }, 1000);
    } else if (state.includes("REQUIRE")) {
      return requestChat(messageText, "fill_slot");
    } else {
      return requestChat(messageText, "request_chat");
    }
  }
}
