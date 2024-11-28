describe('temlpate-spec', () =>{
    it('teste pontos', () => {
        cy.visit('http://127.0.0.1:8000/')
        cy.wait(1000)
        cy.get('#username').type("Mario", {force : true})
        cy.wait(1000)
        cy.get('#password').type("yoshi", {force : true})
        cy.get('button').click({force : true})
        cy.wait(3000)          
        Cypress.on('uncaught:exception', (err, runnable) => {
            console.error('Erro detectado:', err);
            return false; 
          });
        cy.get('#userButton').click();
        cy.wait(1000)
        cy.get('#closeSidebar').click({force : true});
        cy.wait(3000)
        cy.get('.doar').click()
        cy.wait(1000)
        cy.get('input[name="nome_doador"]').type('Doador', { force: true });
        cy.wait(1000)
        cy.get('#email_doador').type('doador@gmail.com')
        cy.wait(1000)
        cy.get('#telefone_doador').type('(81) 99999-9999')
        cy.wait(1000)
        cy.get('#tipo_doacao').type('Resíduos têxteis')
        cy.wait(1000)
        cy.get('#descricao').type('Gostaria de fazer uma doação de resíduos têxteis para a confecção de novos brinquedos.')
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(1000)
        cy.scrollTo('bottom')
        cy.wait(2000)
        cy.visit('http://127.0.0.1:8000/home/')
        Cypress.on('uncaught:exception', (err, runnable) => {
            console.error('Erro detectado:', err);
            return false; 
          });
        cy.get('#userButton').click();
        cy.wait(2000)
        cy.get('#closeSidebar').click({force : true});
        cy.wait(3000)
    })
})