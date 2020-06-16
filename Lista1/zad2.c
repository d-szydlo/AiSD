#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct node {
    int value;
    struct node* next;
};

struct node* create_node(int value){
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    new_node->next = NULL;
    new_node->value = value;
    return new_node;
}

struct list {
    struct node* front;
    struct node* back;
    int size;
};

struct list* create_list(){
    struct list* new_list = (struct list*) malloc(sizeof(struct list));
    new_list->back = NULL;
    new_list->front = NULL;
    new_list->size = 0;
    return new_list; 
}

void push(struct list* l, int value){
    struct node* new_node = create_node(value);
    if (l->front == NULL){
        l->front = new_node;
        l->back = new_node;
    }
    else {
        l->back->next = new_node;
        l->back = new_node;
    }  
    l->size++; 
}

void pop(struct list* l){
    if (l->front != NULL){
        helper = l->front;
        l->front = l->front->next;
        if (l->front == NULL){
            l->back = NULL;
        }
        l->size--;
        free(helper);
    }
}

void push_front(struct list* l, int value){ 
    if (l->front != NULL){
        struct node* new_node = create_node(value);
        new_node->next = l->front->next;
        l->front = new_node;
    } else {
        push(l, value);
    }
    l->size++;
}

void print_list(struct list* l){
    struct node* helper = l->front;
    while (helper != NULL){
        printf("%d ", helper->value);
        helper = helper->next;
    }
    printf("\n");
}

void fill_list(struct list* l){
    for(int i=0; i<1000; i++){
        int helper = rand();
        push(l, helper);
    }
}

struct list* merge_lists(struct list* l1, struct list* l2){
    if (l1->front == NULL) return l2;
    if (l2->front == NULL) return l1;
    l1->back->next = l2->front;
    l1->back = l2->back;
    return l1;
}

int get_by_id(struct list* l, int index){
    struct node* helper = l->front;
    if (index < l->size){
        for (int i=0;i<index;i++){
            helper = helper->next;
        }
        return helper->value;
    } else {
        return -1;
    }
}

void measure_time(struct list* l){
    int const_index = rand()%l->size;
    int var_index;
    clock_t time_period = clock();
    for (int i=0; i<1000; i++){
       get_by_id(l, const_index);
    }
    time_period = clock() - time_period;
    printf("Sredni czas dostepu do tego samego elementu: %lf ms\n", (double) time_period/CLOCKS_PER_SEC*1000);
    time_period = clock();
    for(int i=0; i<1000; i++){
        var_index = rand()%l->size;
        get_by_id(l, var_index);
    }
    time_period = clock() - time_period;
    printf("Sredni czas dostepu do losowego elementu: %lf ms\n", (double)time_period/CLOCKS_PER_SEC*1000);

}

int main(void){
    srand(time(0));
    struct list* my_list1 = create_list();
    struct list* my_list2 = create_list();
    fill_list(my_list1);
    fill_list(my_list2);
    measure_time(my_list1);
    merge_lists(my_list1, my_list2);
}