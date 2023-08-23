function importHistoricalResponses() {
    var form = FormApp.openByUrl('구글폼 주소 입력');
    var formResponses = form.getResponses(); // 설문을 응답한 사람의 수 (form에 response 한 개수)
    var sheet = SpreadsheetApp.getActiveSpreadsheet();

    // 1. 설문을 응답한 모든 사람의 수에 맞춰서 for loop을 돌면서 결과 확인하기
    for ( var user = 0; user < formResponses.length; user++ ){
        // 사용자 별로 결과를 Sheet로 구분하기 위해서 User 0, User 1, User 2와 같은 형태로 새로운 Sheet 만들기
        var responsesSheet = sheet.getSheetByName(`User ${user}`);
        if (responsesSheet != null){sheet.deleteSheet(responsesSheet);}
        responsesSheet = sheet.insertSheet();
        responsesSheet.setName(`User ${user}`);
        
        Logger.log(user)
        var userResponse = formResponses[user];                       // 사용자가 응답한 데이터
        var userResponseByQuestion = userResponse.getItemResponses(); // 사용자가 응답한 질문의 총 개수 (length)
        
        // 2. 첫 번째 Petition 질문부터 마지막 Petition 질문까지 for loop을 돌면서 결과 확인하기
        for ( var question = 0; question < userResponseByQuestion.length; question++ ){
        // 결과물의 형태: [[Q1인 Clearly에 대한 응답], [Q2인 Might에 대한 응답]]
        var surveyOutput = userResponseByQuestion[question].getResponse() 

        var surveyOutputQ1 = surveyOutput[0].toString();            // Q1인 Clearly에 대한 응답
        var surveyOutputQ2 = surveyOutput[1].toString();            // Q2인 Might에 대한 응답

        responsesSheet.appendRow([surveyOutputQ1, surveyOutputQ2]);
        }
    }
}

