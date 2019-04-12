 describe('Django REST Framework / React quickstart app', () => {
  const tweet = {
      text: "Papaco GOD",
      isPublic: true
  };

  before(() => {
      cy.exec("npm run dev")
      // cy.exec("npm run flush")
  });

  it("should be able to fill a web form", () => {
      cy.visit("/", {
          auth: {
              username: 'silverio',
              password: 'lkm-98cd'
          }
      });

      cy
        .get('input[name="text"]')
        .type(tweet.text)
        .should("have.value", tweet.text);
    
      cy
        .get('input[name="isPublic"]')
        .check()
        .should("have.checked", true);

      cy
        .get("form")
        .submit();

      cy
        .visit("/", {
          auth: {
              username: 'silverio',
              password: 'lkm-98cd'
          }
        })
        .get('tr')
        .contains(`${tweet.text}`);
  });
});
