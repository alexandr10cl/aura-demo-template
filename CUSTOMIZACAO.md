# 🎨 Guia de Customização Premium

## 📋 Visão Geral

Este template foi criado para ser facilmente replicado e customizado para diferentes projetos. Toda a customização é feita através do arquivo `static/css/variables.css` - **você não precisa editar outros arquivos CSS**.

## 🎯 Customização Rápida (5 minutos)

### 1. Cores da Marca 

Edite apenas estas variáveis no arquivo `variables.css`:

```css
:root {
    /* Substitua pela cor principal da sua marca */
    --primary-color: #6366f1;        /* Sua cor principal */
    --primary-500: #6366f1;          /* Mesma cor */
    --primary-600: #4f46e5;          /* Versão mais escura */
    --primary-700: #4338ca;          /* Ainda mais escura */
    
    /* Substitua pela cor secundária */
    --secondary-color: #8b5cf6;      /* Sua cor secundária */
    --secondary-500: #a855f7;        /* Mesma cor */
    --secondary-600: #9333ea;        /* Versão mais escura */
}
```

### 2. Fonte da Empresa

```css
:root {
    /* Substitua pela fonte da sua empresa */
    --font-primary: 'Sua Fonte', 'Inter', sans-serif;
    --font-heading: 'Sua Fonte Display', 'Outfit', sans-serif;
}
```

Lembre-se de importar a fonte no início do arquivo `style.css`:
```css
@import url('https://fonts.googleapis.com/css2?family=Sua+Fonte:wght@300;400;500;600;700&display=swap');
```

## 🛠️ Customização Avançada

### Paleta de Cores Completa

Para uma customização mais profissional, você pode ajustar toda a paleta:

```css
:root {
    /* Tons da cor principal */
    --primary-50: #eef2ff;   /* Muito claro */
    --primary-100: #e0e7ff;  /* Claro */
    --primary-200: #c7d2fe;  /* Claro médio */
    --primary-300: #a5b4fc;  /* Médio claro */
    --primary-400: #818cf8;  /* Médio */
    --primary-500: #6366f1;  /* Base (sua cor) */
    --primary-600: #4f46e5;  /* Médio escuro */
    --primary-700: #4338ca;  /* Escuro */
    --primary-800: #3730a3;  /* Muito escuro */
    --primary-900: #312e81;  /* Mais escuro */
}
```

### Espaçamentos

```css
:root {
    /* Ajuste os espaçamentos conforme sua preferência */
    --spacing-xs: 0.25rem;   /* 4px */
    --spacing-sm: 0.5rem;    /* 8px */
    --spacing-md: 1rem;      /* 16px */
    --spacing-lg: 1.5rem;    /* 24px */
    --spacing-xl: 2rem;      /* 32px */
    --spacing-2xl: 3rem;     /* 48px */
    --spacing-3xl: 4rem;     /* 64px */
}
```

### Bordas e Cantos

```css
:root {
    /* Ajuste o arredondamento dos cantos */
    --radius-sm: 0.25rem;    /* Pouco arredondado */
    --radius-md: 0.375rem;   /* Médio */
    --radius-lg: 0.5rem;     /* Arredondado */
    --radius-xl: 0.75rem;    /* Bem arredondado */
    --radius-2xl: 1rem;      /* Muito arredondado */
}
```

## 🚀 Exemplos de Customização por Setor

### E-commerce (Azul/Laranja)
```css
--primary-color: #0ea5e9;
--primary-500: #0ea5e9;
--primary-600: #0284c7;
--primary-700: #0369a1;
--secondary-color: #f97316;
```

### Saúde (Verde/Azul)
```css
--primary-color: #10b981;
--primary-500: #10b981;
--primary-600: #059669;
--primary-700: #047857;
--secondary-color: #06b6d4;
```

### Financeiro (Azul Escuro/Dourado)
```css
--primary-color: #1e40af;
--primary-500: #1e40af;
--primary-600: #1d4ed8;
--primary-700: #1e3a8a;
--secondary-color: #d97706;
```

### Tecnologia (Roxo/Ciano)
```css
--primary-color: #8b5cf6;
--primary-500: #8b5cf6;
--primary-600: #7c3aed;
--primary-700: #6d28d9;
--secondary-color: #06b6d4;
```

## ✅ Checklist de Customização

- [ ] Alterar cores principais (primary e secondary)
- [ ] Definir fonte da empresa
- [ ] Ajustar logo/nome da empresa nos templates
- [ ] Personalizar textos dos exemplos
- [ ] Testar responsividade em diferentes dispositivos
- [ ] Verificar acessibilidade das cores escolhidas