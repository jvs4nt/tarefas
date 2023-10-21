package br.com.salesforce.beans;

public class Produto {

	
	private String nomeProduto;
	private String marca;
	private int idProduto;
	private String descricao;
	private double preco;
	private String categoria;
	
	public Produto() {
		super();
	}

	public Produto(String nomeProduto, String marca, int idProduto, String descricao, double preco, String categoria) {
		super();
		this.nomeProduto = nomeProduto;
		this.marca = marca;
		this.idProduto = idProduto;
		this.descricao = descricao;
		this.preco = preco;
		this.categoria = categoria;
	}

	public String getNomeProduto() {
		return nomeProduto;
	}

	public void setNomeProduto(String nomeProduto) {
		this.nomeProduto = nomeProduto;
	}
	

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public int getIdProduto() {
		return idProduto;
	}

	public void setIdProduto(int idProduto) {
		this.idProduto = idProduto;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public double getPreco() {
		return preco;
	}

	public void setPreco(double preco) {
		this.preco = preco;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}
	
	
	
	
}
