describe('template spec', () =>{
    it('teste doar', () => {
        cy.visit('http://127.0.0.1:8000/doar/')
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

    })
    it('teste doar NF', () =>{
        //Este código aqui se refere a um teste não funcional
        cy.visit('http://127.0.0.1:8000/doar/')
        cy.wait(1000)
        cy.get('input[name="nome_doador"]').type('Doador', { force: true });
        cy.wait(1000)
        cy.get('#email_doador').type('doador&gmail.com')
        cy.wait(1000)
        cy.get('#telefone_doador').type('(81) 99999-9999')
        cy.wait(1000)
        cy.get('#tipo_doacao').type('Resíduos têxteis')
        cy.wait(1000)
        cy.get('#descricao').type('Gostaria de fazer uma doação de resíduos têxteis para a confecção de novos brinquedos')
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(3000)
    })
})