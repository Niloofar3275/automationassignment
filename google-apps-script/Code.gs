function createAndSendForm() {
  /*
  Reading the updated "top 5 cast members" spreadsheet file
  */
  var top5CastSheet = SpreadsheetApp.openById("1Tjh9mgQ9fZ-377XOV22OE5eBpOSBJkfzv131hMQBMjI").getSheetByName('Sheet1');
  var top5Cast = new Array();
  var i;
  for (i = 1; i <= 5; i++) {
    top5Cast.push(top5CastSheet.getRange(i, 1).getValue());
    Logger.log(top5Cast[i - 1]);
  }

  /*
  Creating a brand new form based on the list we just retrieved  
  */
  var today = new Date();
  var todayDate = today.getFullYear() + "/" + today.getDate() + "/" + (today.getMonth()+1);
  var item = "Vote a Cast Member (Updated " + todayDate + ")";
  var form = FormApp.create(item)
    .setTitle(item);

  item = "Choose an actor/actress";
  form.addCheckboxItem()
    .setTitle(item)
    .setChoiceValues(top5Cast);
  
  // We need keep the PublishedURL of our form, for later use(sending it to people)
  formURL = form.getPublishedUrl();
  Logger.log(formURL);

  /*
  Reading the email list, from the specified spreadsheet
  */
  var emailListSheet = SpreadsheetApp.openById("1a-9JV8D3ZidScumSw50rN5_C9T6LqFzd0WffkdTtcoY").getSheetByName('Sheet1');
  var emailList = emailListSheet.getDataRange().getValues();
  // Joining the email addresses with ','
  var recipient = "";
  for (i = 0; i < emailList.length; i++){
    if (i != 0)
      recipient += ","
    recipient += emailList[i][0];
  }

  // Sending email
  message = "Here is a brand new poll for you: " + formURL;
  MailApp.sendEmail(recipient, "Cast member poll (Updated " + todayDate + ")", "", {htmlBody: message});
}